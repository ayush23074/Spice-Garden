# Deploy This Django App With Netlify (Proxy) + Render (Backend)

Netlify cannot run a long-lived Django server directly.  
For this codebase, the reliable setup is:

- Django app runs on Render (already configured by `render.yaml`)
- Netlify sits in front as a proxy/custom domain

## 1) Deploy backend to Render

1. Push this repo to GitHub.
2. In Render, create a Web Service from the repo.
3. Render should detect `render.yaml`.
4. Set required env vars in Render:
   - `DEBUG=False`
   - `ALLOWED_HOSTS=jango-app.onrender.com,<your-netlify-site>.netlify.app`
   - `CSRF_TRUSTED_ORIGINS=https://<your-netlify-site>.netlify.app`
   - DB vars (`PROD_DB_*`) as needed.

## 2) Deploy the same repo to Netlify

1. In Netlify, add a new project from this repo.
2. Build command can stay empty (or use value from `netlify.toml`).
3. Netlify build base is `netlify` and publish directory is `.` (already set in `netlify.toml`).
4. Deploy.

`netlify.toml` proxies all paths to:

`https://jango-app.onrender.com`

If your Render service URL is different, update `netlify.toml` accordingly.

## Important: Deploy branch

Set Netlify to deploy the branch that contains `netlify.toml` changes (`old-code` in this repo right now), or merge these changes into `main`.

## 3) Verify

1. Open your Netlify URL.
2. Test login/register/form submission.
3. If CSRF error appears, double-check:
   - `CSRF_TRUSTED_ORIGINS` includes exact Netlify URL with `https://`
   - `ALLOWED_HOSTS` includes Netlify host without scheme
