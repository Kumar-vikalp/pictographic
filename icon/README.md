
# Pictographic Icon Generator Script

This Python script demonstrates how to programmatically generate icons using the **Pictographic AI** service. It sends a prompt to their API and returns JSON data describing the generated icon(s).

---

## ⚡ Features

* Uses Python `requests` to interact with a REST API.
* Sends a **custom prompt** to generate icons.
* Skips credit checks (`skip_credit_check`) for free plan usage.
* Returns JSON output containing generated icon data.
* Prints JSON in a readable, formatted way using `json.dumps`.

---

## 🧰 Techniques & Libraries Used

* **`requests`** – popular HTTP library for Python for making REST API requests. [Documentation](https://docs.python-requests.org/en/latest/)
* **`json`** – standard Python library to parse and pretty-print JSON. [Documentation](https://docs.python.org/3/library/json.html)
* Custom headers including `User-Agent` and `Referer` to simulate browser requests.
* Skipping credit checks programmatically with `skip_credit_check` key.

---

## ⚠️ Notes on Usage

* The script is configured to use the **Free/Starter Plan**. This plan provides **limited credits and downloads**, but attribution is required.
* You can change the prompt by editing the `json_data['prompt']` value.
* Email is optional but can be set for tracking or API purposes.
* The script prints JSON output; it does **not save images automatically**. You can use the URLs in the output for manual download.

---


* **generated/**: Optional directory to save images if you modify the script to download them.
* **main.py**: Core Python script interacting with the Pictographic API.
