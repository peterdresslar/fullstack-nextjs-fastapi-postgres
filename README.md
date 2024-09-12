# Next.js Flask Postgres Starter

This project extends Vercel's `nextjs-flask` template to demonstrate:
1. Interaction with the Flask API (the Next app from the base example does not actually interact with the Flask API)
2. A simple Postgres database creation, migration, and seeding workflow, connected to the Flask app using Flask-Migrate

## Introduction

This is a hybrid Next.js + Python app that uses Next.js as the frontend and Flask as the API backend. It demonstrates how to integrate a Postgres database into this stack, including setup, migrations, and seeding.

## Key Features

- Next.js frontend
- Flask API backend
- Postgres database integration
- Database migration and seeding workflow
- Can run locally or be hosted on Vercel (or other platforms)

## Requirements

The critical external requirement for this project is a Postgres database and a connection string stored as an environment variable. The project will look for the environment variable in a `.env` file (using Python's `dotenv`) when run locally, or in the hosting platform's environment variables (e.g., Vercel's production environment variables) when deployed.

**Note on Security**: The database security in this example is basic and should be enhanced for production use.

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fullstack-nextjs-flask.git
   cd fullstack-nextjs-flask
   ```

2. Install dependencies:
   ```
   pnpm install
   pip install -r requirements.txt
   ```

3. Set up your Postgres database and add the connection string to your `.env` file:
   ```
   POSTGRES_URL=postgresql://username:password@host:port/database?sslmode=require
   ```

4. Initialize the database:
   ```
   pnpm run init-db
   pnpm run migrate-db
   pnpm run upgrade-db
   pnpm run seed-db
   ```

5. Run the development server:
   ```
   pnpm run dev
   ```

6. Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Deployment

This project can be easily hosted on Vercel, but it's also possible to host it on other platforms. Here are the steps for deploying to Vercel:

1. Push your code to a GitHub repository.

2. Sign up for a Vercel account if you haven't already.

3. In Vercel, click "New Project" and import your GitHub repository.

4. In the configuration step:
   - Framework Preset: Select Next.js
   - Build Command: Use the default (`next build`)
   - Output Directory: Use the default (`.next`)
   - Install Command: Change to `pnpm install`

5. In the Environment Variables section, add your `POSTGRES_URL`.

6. Deploy the project.

For other platforms, ensure that:
- Both the Next.js frontend and Flask backend are deployed.
- The `POSTGRES_URL` environment variable is set.
- Python dependencies from `requirements.txt` are installed.
- Database migrations are run on deployment.

## How It Works

The Python/Flask server is mapped into the Next.js app under `/api/`. This is implemented using `next.config.js` rewrites to map any request to `/api/:path*` to the Flask API, hosted in the `/api` folder.

On localhost, the rewrite will be made to `127.0.0.1:5328`, where the Flask server runs. In production, the Flask server is hosted as serverless functions.

The Postgres database is accessed through SQLAlchemy in the Flask backend, demonstrating basic CRUD operations and migrations.

## Learn More

- [Next.js Documentation](https://nextjs.org/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Vercel Deployment Documentation](https://vercel.com/docs)
