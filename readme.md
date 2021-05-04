# Duplicate Line Below
Believe it or not, this title isn't clickbait. With a single command, you can duplicate a line as though in place. 
To elaborate; Sublime's "duplicate_line" adds a new line below the current one and moves down to it, keeping the column index invariant. As an Npp graduate, I felt somewhat disappointed by this so I created a plugin which will duplicate the line as before, but move the cursor to the line above.

## Why
As I said, I recently moved from Notepad++ but, more importantly, this shortcut is expedient in cases where you would be commenting a(/some) line(s) to perhaps revert to later because you'd only have to change line manually once in order to make the comment whereas (assuming you were going to continue editing lower in the page after this adjustment) Sublime's builtin seems more appropriate for implementing artificial iteration of some sort.

###### Todo
Add autocomment