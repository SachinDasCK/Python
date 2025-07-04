from website import create_app # importing website package and grab the create_app function to actuale create and run an application 

app =  create_app()

if __name__ == "__main__": # it mean only if we run this file - it should run and not importing 
    app.run(debug=True)    # run flask application, debug = true helps to rerun webserver everytime we make changes to python code
