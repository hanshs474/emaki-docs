# HTTP API

Base URL `https://emaki.ai`. Every call is a `POST` with `Authorization: Bearer <key>` ([create a key](https://emaki.ai/settings/apikeys)).

## Submit a run

```bash
curl -s -X POST https://emaki.ai/api/video/ai \
  -H "Authorization: Bearer $EMAKI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "a fox trotting through fresh snow at dawn, tracking shot",
    "model": "seedance_2_5",
    "parameters": {"duration": 8, "resolution": "720p", "aspect_ratio": "9:16"}
  }'
```

| Field | Value |
|---|---|
| `prompt` | What happens in the shot (Japanese or English) |
| `model` | A model id from the [models](models.md) table, e.g. `seedance_2_5` |
| `parameters` | Optional; anything left out takes the model's default |

Answer: `200 {"success": true, "data": {"id": "<videoId>", "status": "generating", ...}}`. Keep `data.id`.

The same endpoint makes images: pass an image model id such as `nano_banana_2_lite`.

## Poll it

```bash
curl -s -X POST https://emaki.ai/api/video/status \
  -H "Authorization: Bearer $EMAKI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"videoId": "<videoId>"}'
```

Answer: `200 {"success": true, "data": {"id": "...", "status": "generating" | "completed" | "failed", "videoUrl": "...", "failureCode": ...}}`.

Poll every 5 seconds. On `completed` the result URL is in `videoUrl` (images too). On `failed`, `failureCode` says why. Video can wait in a queue first; the SDKs give up after 15 minutes by default.

## Credit balance (free)

```bash
curl -s -X POST https://emaki.ai/api/user/get-user-credits -H "Authorization: Bearer $EMAKI_API_KEY"
```

Answer: `{"code": 0, "data": {"remainingCredits": 120, "hasPurchasedCredits": true}}`. A refusal is HTTP 200 with `{"code": -1, "message": ...}`, so read `code`, not the status line.

## Errors from the submit call

The body is `{"error": "...", "code"?: "..."}`.

| HTTP | Meaning | Python SDK raises |
|---|---|---|
| 401 | No key, or the key is invalid | `AuthError` |
| 402 | `Insufficient credits` | `QuotaError` |
| 403 | This model needs a purchase on the account | `PlanError` |
| 409 | `Video generation is already in progress`: one run at a time per account | `BusyError` |
| 429 with `code: content_cooldown` · 400 with `code: content_blocked` | The prompt was refused | `RejectedError` |
| other 400 | A parameter is out of range; `error` says which | `EmakiError` with that message |
| 5xx | Server side; retry later | `EmakiError` |
