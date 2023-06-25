 Here are some examples of API calls and the corresponding responses

1. GET `/api` - Get the word from the database:
   - Request: `GET /api`
   - Response: `200 OK`
   ```json
   {
     "word": "Test"
   }
   ```

2. POST `/admin` - Update the word in the database:
   - Request: `POST /admin`
   - Body: `word=New Word`
   - Response: `200 OK`
   ```html
   <html>
     <body>
       <p>Word updated successfully.</p>
     </body>
   </html>
   ```

3. GET `/admin` - Access the admin portal:
   - Request: `GET /admin`
   - Response: `200 OK`
   ```html
   <html>
     <body>
       <form action="/admin" method="post">
         <input type="text" name="word" placeholder="Enter a new word">
         <button type="submit">Update Word</button>
       </form>
     </body>
   </html>
   ```
