Requirement: nltk

Installation: pip3 install nltk

###################################

To run example.py 

1. open command line, type the following command,

  **python3 example.py "book_title" "book_abstract"

Note: Extract_keyword.py is built using Flask

################################################

To run Extract_keyword.py

1. open command line:
   Type **"python3 Extract_keyword.py"
   
   After running this command: the result will be as the following
   
 * Serving Flask app "test" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 599-400-286
 
 From the result, copy http://127.0.0.1:5000/.

2. Open new Tab in command line, and then type the following command,

   curl --header "Content-Type: application/json" --request POST --data '{"title":"This is title","abstract":"Resources for    the non-English languages are scarce and this paper addresses this problem in the context"}' http://127.0.0.1:5000/
    
   **The value of title and abstract can be changed!!!!!**

