showHighScore = -- Py export for end game show high score
userInput = -- Py export for user input
currentUser = -- Py export for current user ID

CREATE TABLE Users (
    userID CHAR(4) NOT NULL,
    userName VARCHAR(10) NOT NULL,
    highScore 0,
    userID PRIMARY KEY,
    highScore FOREIGN KEY
)

SELECT highScore, userName, userID; 
FROM Users; 
WHERE userID LIKE currentUser; 
IF userInput LIKE showHighScore; 
ORDER BY highScore LIMIT 1

FUNCTION checkPassword (
    SELECT un, email, userID;
    FROM Users;
    WHERE pass LIKE userPass;
    IF userInput NOT NULL;
    ORDER BY userID limit 1
)

FUNCTION checkUserID (
    SELECT un, email, pass, highScore, userID;
    FROM Users;
    WHERE checkUserID(id) LIKE userID;
    IF userInput NOT NULL;
    ORDER BY userID LIMIT 1
)

