rm functions.zip
cd functions
zip -q -r ../functions.zip .
cd ..
cd venv/lib/python3.8/site-packages/
zip -q -r ../../../../functions.zip .
cd ../../../../