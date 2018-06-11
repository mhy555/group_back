## Front-end

1 Go to automated-story-telling folder

   ```
   > cd automated-story-telling
   ```

2 Install all the dependencies.

   ```
   > npm install
   ```

3 Run the programme. Changes made in code will be automaticly refreshed on webpage once saved.

   ```
   > npm run dev
   ```

## Back-end

1 Go to server floder

   ```
   > cd server
   ```

2 Install jpype

   Go to server/src/JPype1-0.6.2

   ```
   > setup install
   ```

3 Install stanford-parser

   Go to server/src/stanford-parser-python-r22186/3rdParty

   ```
   > rake download; rake setup
   ```

4 Install dependencies

   ```
   > pip install flask-cors
   > pip install mysql-python
   > pip install image
   > pip install Pillow
   > pip install nltk
   > pip install pattern
   > pip install numpy
   > pip install requests
   > pip install BeautifulSoup4
   ```

5 Install nltk dependencies

   ```
   > python
   >>> import nltk
   >>> nltk.download('maxent_ne_chunker')
   >>> nltk.download('words')
   >>> nltk.download('punkt')
   >>> nltk.download('averaged_perceptron_tagger')
   >>> nltk.download('wordnet')
   ```

6 Run the service

   Go to server/src/service

   ```
   > FLASK_APP=service.py flask run --host=127.0.0.1
   ```
