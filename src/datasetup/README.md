# NL2SQL Sample Data

![I stand with Israel](../../docs/IStandWithIsrael.png)

This folder is dedicated to storing the sample data created post the Azure SQL Server/Database setup. The steps below guide you through the process of setting up the environment and creating the sample data.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Hire me

Please send [email](mailto:kingdavidconsulting@gmail.com) if you consider to **hire me**.

[![buymeacoffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/vyve0og)

## Give a Star! :star

If you like or are using this project to learn or start your solution, please give it a star. Thanks!

## Environment Setup

1. **Create .env File**: Create a `.env` file in this directory. This file will store your Azure SQL Server/Database credentials.

    Here is a sample of what your `.env` file should look like:

    ```
    SERVER_NAME=<server_name>.database.windows.net
    DATABASE_NAME=<database_name>
    SQLADMIN_USER=<user_name>
    SQL_PASSWORD=<password>
    ```

    Replace `<server_name>`, `<database_name>`, `<user_name>`, and `<password>` with your actual Azure SQL Server/Database credentials.

2. **Create Python Virtual Environment**: Navigate to the root of the project and run the `create-venv.sh` script. This script sets up a Python virtual environment for the project. After running the script, reload your VSCode workspace to apply the changes.

## Data Creation

Run the `create_data.py` script. This script creates a table named `ExplorationProduction` in your Azure SQL Database and populates it with fake data.

```python
    python create_data.py
```


After running the script, your `ExplorationProduction` table should be populated with the sample data.

That's it! You have now set up your environment and created your sample data. You can now proceed with your NL2SQL tasks..
