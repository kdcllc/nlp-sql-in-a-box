
import time
import asyncio

from dotenv import load_dotenv

from util import setup_kernel, get_result_from_database

def main():

    load_dotenv()

    # Create a new kernel
    kernel, plugin = setup_kernel()
    
    # Starting the Conversation
    print("....Welcome to the Kiosk Bot!! I am here to help you with your queries. Type 'q' at anytime to exit.")

    while(True):
        # Taking Input from the user through the Microphone
        query = input("Enter the query: ")
        print("The query is: {}".format(query))
        
        if query.lower() == 'q':
            break

        sql_query = asyncio.run(kernel.run(plugin["nlpToSQLPlugin"], input_str=query)).result
        print("The SQL query is: {}".format(sql_query))

        # Use the query to call the database and get the output
        result = get_result_from_database(sql_query)
        # Speak out the result to the user
        print("The result of your query is: {}".format(result))


if __name__ == "__main__":
    start = time.time()
    main()
    print("Time taken Overall(mins): ", (time.time() - start)/60)