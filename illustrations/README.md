
# Pictographic Illustrations Generation 

## Description
takes upto (120 sec) to generate an Illustrations. 
This project demonstrates how the Illustrations generation workflow of **Pictographic** can be automated and monitored programmatically. Instead of using the website interface, the script directly interacts with the backend services used by the platform.

The workflow submits a generation request, retrieves a **prompt identifier**, and then watches the **Firebase Realtime Database** for updates until the generated images become available. Once the generation completes, the script outputs the image URLs and reports how long the entire generation process took.

This repository focuses on understanding and reproducing the **client-side workflow** used by the platform rather than interacting with internal or undocumented APIs.

---

## What This Project Demonstrates

This project reproduces the same process the browser performs when a user generates Illustrations on the Pictographic website.

Instead of clicking buttons in the UI, the workflow:

1. Submits a generation request
2. Receives a prompt/job identifier
3. Watches the backend database for updates
4. Detects when images are generated
5. Outputs the image URLs and timing information

The goal is to illustrate how real-time systems can be monitored externally when their client architecture relies on observable APIs and databases.

---

## Architecture Overview

The Illustration generation process is built around three major components:

* The **Pictographic API**
* A **background generation worker**
* **Firebase Realtime Database**

These components communicate together to process prompts and publish generated results.

High-level flow:

User Request
→ Pictographic API
→ Image Generation Worker
→ Firebase Realtime Database
→ Client receives updates

---

## Step‑by‑Step Workflow

### 1. Prompt Submission

The workflow begins by submitting a request containing the Illustration prompt, style configuration, and metadata such as dimension and optional email.

Once the request is accepted, the API returns a **unique prompt identifier**.
This identifier represents the generation job.

Example identifier returned by the service:

* OnQxcS-qAJK0hlL7GW9

This value becomes the key used to track the generation progress.

---

### 2. Job Tracking via Firebase

After receiving the identifier, the system begins monitoring the Firebase Realtime Database entry associated with the job.

Each prompt is stored inside a structure similar to:

/prompts
    /prompt_id
        status
        prompt
        images

Initially, the entry contains metadata about the request and a status indicating that generation is still in progress.

---

### 3. Real‑Time Updates

The generation workers responsible for creating the Illustrations update the database once images are produced.

When new images become available, the Firebase entry receives additional fields:

image_1
image_2
image_3
image_4

Each field contains the URL of the generated asset.

Because Firebase supports real‑time updates, the client can continuously monitor the job status and detect when each image becomes available.

---

### 4. Image Discovery

As images appear in the database entry, their URLs become accessible.

Example generated assets:

* [https://generated.pictographic.io/transparency/XUSRaGxHT7wmQk8fKS3xf9.png](https://generated.pictographic.io/transparency/XUSRaGxHT7wmQk8fKS3xf9.png)
* [https://generated.pictographic.io/transparency/nALiXnodEkQKqvmhWVKgie.png](https://generated.pictographic.io/transparency/nALiXnodEkQKqvmhWVKgie.png)
* [https://generated.pictographic.io/transparency/8mkawbnyeB3TtAAykCATMY.png](https://generated.pictographic.io/transparency/8mkawbnyeB3TtAAykCATMY.png)
* [https://generated.pictographic.io/transparency/A6PKGBHieyeDjLgiTg3KMR.png](https://generated.pictographic.io/transparency/A6PKGBHieyeDjLgiTg3KMR.png)

These URLs point to the final generated PNG files hosted by the platform.

---

### 5. Completion Detection

Once all expected images are available, the workflow considers the generation complete.

At this point the script reports:

• All generated image URLs
• Total generation time

Example completion output:

Image 1 generated
Image 2 generated
Image 3 generated
Image 4 generated

All images generated successfully.

Total generation time: approximately 120 seconds.

---

## Why Firebase Is Used

Firebase Realtime Database enables **live data synchronization** between backend services and clients.

Instead of repeatedly querying the API for job status, the system simply watches the database entry associated with the prompt.

Benefits include:

• Near real‑time updates
• Reduced API polling
• Simplified state management for clients
• Immediate UI updates in the browser

More information about this model can be found here:

[https://firebase.google.com/docs/database](https://firebase.google.com/docs/database)

---

## Observations About the System Design

This workflow reveals several interesting aspects of the platform architecture:

1. **Job‑based processing**

Image generation is treated as a queued background task rather than a synchronous API request.

2. **Database‑driven state updates**

Instead of pushing updates through a proprietary event system, the backend writes generation results directly to Firebase.

3. **Client‑observable workflow**

Because the browser must observe these updates to display generated images, the entire process becomes externally observable through the same endpoints.

4. **Prompt identifier as job handle**

The prompt ID returned during submission acts as the unique key for tracking generation progress.

---

## Result

Using this workflow, the entire generation lifecycle can be monitored programmatically:
```
Submit prompt
→ obtain prompt identifier
→ monitor Firebase entry
→ detect generated images
→ retrieve final asset URLs
→ measure generation time
```
This repository serves as a technical exploration of how client‑side systems interact with real‑time databases to track asynchronous generation pipelines.

