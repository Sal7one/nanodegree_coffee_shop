# Coffee Shop Full Stack

# User data

# Barista Token:

```

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpyM3JhdWdQRWY4OWRGVmhxb0c2RiJ9.eyJpc3MiOiJodHRwczovL2Rldi05ZzBsdi05OC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBmZjc4YWEwZjg2NjQwMDY5MmIxMzllIiwiYXVkIjoiZHJpbmtlciIsImlhdCI6MTYyNzM1NTM0NCwiZXhwIjoxNjI3MzYyNTQ0LCJhenAiOiIxRk5RTjdMU2ZWNVlrTkI2eE01RmFpQmhXWXNGVHQ0NyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.SumknZEB5JRR_eR8L-D0-Be5i-gjt2-QZMWvqvnISIUwaK5GXlwOXMQGwP4kE4u0tupwO-IprB1ydlj7-NUl79m8RLmmyVmy-nq7gOgqqkWUYQQQFMsxV5eyGJXKbgVsFK4f_EbxKQS0EfAwtDrLPEEhJZ8O4uyt7IbKMoiczVuuTsS1lo1hhLps8XEo37RsbGyqhsgBgWu9r3Jx1keu9cVmmvxm4HpamQryrk0AvLkjOd_8ah-Aa2jwJy99LOgszbos59G8USu1V4QxlHJLruh20k__IoQd4aQVazuswHO_QWZDHosakv4f7TYkOCrxfdfV-lpWzAk3Xot5nebS0w
```

# Magner Token:

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpyM3JhdWdQRWY4OWRGVmhxb0c2RiJ9.eyJpc3MiOiJodHRwczovL2Rldi05ZzBsdi05OC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBmZjc2ZDhjNzI0MDUwMDcxYjU1ZTgwIiwiYXVkIjoiZHJpbmtlciIsImlhdCI6MTYyNzM1NTE3OSwiZXhwIjoxNjI3MzYyMzc5LCJhenAiOiIxRk5RTjdMU2ZWNVlrTkI2eE01RmFpQmhXWXNGVHQ0NyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.T0F1GtNBz7GMlkAxhU8qroHVcKqb0NgzADWrbqE99WH5Qch_BZOofccU8k-EPc0yS6c0H0hYsRXutni7AUL-aMX3fSHvaoK40xxXHElLH7jvxj3KRDWzP5wbEIOxP5jZgA1xsveBbBQg6Hk9Cy74cksKBZLg3AbKOgjMsKn6rG6D3heI3cLovUlCTQzKyXViQsrw5a5fRsyg6Dv4bYSutkaNZsjk3Ql3LGjD7rXMw314a8o-mmbKtIqjk7p5qd1cLCDgOm__BMlcc4YVx2xbiEgO5A_jRaKF9A_JDgiyIjZCpP3qgu5ufGOKj5sXNQckvnilgsJ_oddFcgDhk8EaHA
```

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

## Tasks

There are `@TODO` comments throughout the project. We recommend tackling the sections in order. Start by reading the READMEs in:

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask server with a pre-written SQLAlchemy module to simplify your data needs. You will need to complete the required endpoints, configure, and integrate Auth0 for authentication.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. You will only need to update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app.

[View the README.md within ./frontend for more details.](./frontend/README.md)
