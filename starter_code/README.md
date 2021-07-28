# Coffee Shop Full Stack

# User data

# Barista Token:

```

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpyM3JhdWdQRWY4OWRGVmhxb0c2RiJ9.eyJpc3MiOiJodHRwczovL2Rldi05ZzBsdi05OC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBmZjc4YWEwZjg2NjQwMDY5MmIxMzllIiwiYXVkIjoiZHJpbmtlciIsImlhdCI6MTYyNzQwNjk5MCwiZXhwIjoxNjI3NDkzMzkwLCJhenAiOiIxRk5RTjdMU2ZWNVlrTkI2eE01RmFpQmhXWXNGVHQ0NyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.hgBJfTaN7o5p2YK8dsJaVlEuXLXnIPD3Liro72q52T5drGBv_2oJT4m15gAUgUxwzRJfpCThDm_Fse_zEAZsqK-8RbbTI_gbq0qTnlVOl4WeS-qNhSo68-srRZKIaRYOsfWCWAAfQ1inUjR_-LTzRDzgfchLuQ_rc9cNETRmCCUhrUEpu4KpD-f8zW2PFME0Y1CKgrRgztybCxO_FJ1tYLaoa61cw6lCFOnYS1kDv9D0trr-Rhzt0G30SBqWPG2p3Gybxdf0I_GiOrV8pzHAg5sw8CQNu4Hnif6ip4N1QPAbMf1Rw98RK67iOjg9UowQYchaIWeVNT49Zov5Mol6uA
```

# Magner Token:

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpyM3JhdWdQRWY4OWRGVmhxb0c2RiJ9.eyJpc3MiOiJodHRwczovL2Rldi05ZzBsdi05OC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBmZjc2ZDhjNzI0MDUwMDcxYjU1ZTgwIiwiYXVkIjoiZHJpbmtlciIsImlhdCI6MTYyNzQwNjkxNiwiZXhwIjoxNjI3NDkzMzE2LCJhenAiOiIxRk5RTjdMU2ZWNVlrTkI2eE01RmFpQmhXWXNGVHQ0NyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.mMneVQ-CarV9CQF1hO9C7om_opFNRxzYNl5HC-IVNmTIdbbVA08_gJ3E2eo9zMrYTRk6alkZSJsUTs34VTGXBnIjEiDYcKa9BRO6EJfZ_d8jJn0KLA4ysJuMfhm38G1RJ216W3OjhVMx9tXELb6Q_V6VtLYDd7gI1oIUWvTHdoofClBCL3d3LhADz5ts89pZ2YyeEFED_O8rfjePoslDgS5Fc761JD6-G8gbx-Agm-lhOEYtMjbBUqy4QcC5iwP-6IM4AkI1vcTLgYIjfsdvrGfw6aM3xx_9XTcgmYtB-kjnMOfAbE3x2IvQTAjjUQOs--yU_04mL9LXsYz8VnP4eQ
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
