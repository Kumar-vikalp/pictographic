

# Pictographic AI Icon Generator

This repository contains Python scripts to generate and watch AI-generated icons from [Pictographic](https://www.pictographic.io). The scripts demonstrate automated prompt submission, real-time status tracking via Firebase, and optional image downloading.

---

## Interesting Techniques

* **Realtime updates using Firebase Realtime Database** – Uses Firebase JSON REST endpoints to watch changes in generated prompts. [MDN Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) is leveraged for repeated GET requests.
* **Python `requests` library** – Handles both POST and GET HTTP requests efficiently. [Requests documentation](https://docs.python-requests.org/en/latest/).
* **Dynamic image URL tracking** – Tracks generated image URLs without saving to disk initially, showing how to manage state in loops.
* **Timer calculation** – Uses Python `time` module to calculate total generation time.
* **Directory handling** – Uses `os.makedirs` for creating structured folders if saving images is enabled. [os.makedirs](https://docs.python.org/3/library/os.html#os.makedirs)

---

## Not-Obvious Technologies

* **Firebase Realtime Database** – Provides a lightweight, JSON-based API for real-time updates without setting up a full WebSocket or server.
* **JSON-based API communication** – Combines POST payloads for prompt submission and GET requests for streaming updates.
* **Optional image handling** – While saving images is optional, the script is ready to scale for local caching or pre-processing pipelines.

---

## External Libraries

* [requests](https://pypi.org/project/requests/) – For HTTP requests in Python.
* [time](https://docs.python.org/3/library/time.html) – Built-in module for tracking execution time.
* [os](https://docs.python.org/3/library/os.html) – Built-in module for file and directory management.

---

**generated_images/**: Only created if image downloading is enabled. Stores PNG files generated from prompts.


## 💸 Pictographic Pricing Overview

The service offers multiple tiers, but most are **quite expensive** compared to the free Starter plan:

| Plan             | Price              | AI Credits    | Downloads    | Formats                           | Attribution    |
| ---------------- | ------------------ | ------------- | ------------ | --------------------------------- | -------------- |
| **Free Plan**    | $0                 | 6 lifetime    | 10 per month | PNG only                          | ✅ Required     |
| **Starter Plan** | $60 / $30 yearly   | None          | Unlimited    | SVG + PNG                         | ❌ Not required |
| **Pro Plan**     | $204 / $102 yearly | 100 per month | Unlimited    | All formats                       | ❌ Not required |
| **Pro+ Plan**    | $408 / $204 yearly | 400 per month | Unlimited    | All formats + color customization | ❌ Not required |
| **API Access**   | Custom             | Unlimited     | Unlimited    | SVG + PNG                         | ❌ Not required |

> ⚠️ The **Free Plan** is extremely limited (6 lifetime AI credits and 10 downloads per month) but **costs nothing**, while full-featured plans start at **$60/year** and can go up to **$408/year**. Using this script, you can bypass paid limitations to generate icons programmatically, though attribution is required under the free plan.
> ```

