## Answer Sheet: Lab09

**Question 1:** What is the purpose of the `@app.route('/health')` decorator in the code?

**Answer:**The decorator maps the URL /health to a function.

That function returns a quick status response.

This is commonly used for monitoring and ensuring the app is healthy.




----------------
**Question 2:** In Jinja2, what is the difference between `{{ my_variable }}` and `{% for item in my_list %}`?

**Answer:**{{ ... }} → outputs a value.

{% ... %} → controls logic/flow (loops, conditions, blocks).




----------------
**Question 3:** In `app.py`, why is it important to use `(?, ?)` and pass the variables as a tuple in the `conn.execute()` command instead of using f-strings to put the variables directly into the SQL string? What is this technique called?

**Answer:**f-strings → unsafe, can lead to SQL injection.

(?, ?) with tuple → safe, prevents injection and handles special characters correctly.

Technique name → SQL parameterization / prepared statements.




----------------
**Question 4:** What is the purpose of `event.preventDefault()` in the JavaScript code? What would happen if you removed that line?

**Answer:**With event.preventDefault() → the form is handled by JavaScript, allowing AJAX submission without page reload.

Without it → the browser reloads the page immediately, bypassing the AJAX logic.




----------------
**Question 5:** In the `Dockerfile`, why is the `CMD` `["flask", "run", "--host=0.0.0.0"]` necessary? Why wouldn't the default `flask run` (which uses host 127.0.0.1) work?

**Answer:**In the Dockerfile, the command CMD ["flask", "run", "--host=0.0.0.0"] is necessary because by default Flask binds to 127.0.0.1, which only accepts connections from inside the container itself. When running in Docker, the application needs to listen on all network interfaces (0.0.0.0) so that the port mapping (for example -p 8080:5000) allows external clients on the host machine to reach the Flask server.

If you only use the default flask run with 127.0.0.1, the server would not be accessible from outside the container, even though the container port is published, because the application is not listening on the container’s external interface.




----------------
**Question 6:** In the `docker-compose.yml` setup, Nginx is configured to `proxy_pass http://flask-app:5000`. How does the Nginx container know the IP address of the `flask-app` container?

**Answer:**Docker Compose creates a shared network for services.

Each service name (like flask-app) acts as a DNS hostname.

Nginx resolves flask-app to the container’s IP automatically, so you don’t need to hardcode addresses.



