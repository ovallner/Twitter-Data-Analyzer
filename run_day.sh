if [[ "$#" -eq 1 ]]; then
    echo "Importing tweet data to MongoDB..."
    ./txt_to_mongo.py $1

    echo "Creating CSV from tweet data..."
    ./expanded_csv_generator.py $1

    echo "Running analysis on tweet data..."
    ./analysis.py $1

    echo "Process complete."

elif [[ "$#" -eq 2 ]]; then
    echo "Importing tweet data to MongoDB..."
    ./txt_to_mongo.py $1 $2

    echo "Process complete."

elif [[ "$#" -eq 3 ]]; then
    echo "Importing tweet data to MongoDB..."
    ./txt_to_mongo.py $1 $2

    echo "Creating CSV from tweet data..."
    ./expanded_csv_generator.py $1 $2 $3

    echo "Running analysis on tweet data..."
    ./analysis.py $1 $2 $3

    echo "Process complete."

else
    echo "Invalid number of arguments"
fi
