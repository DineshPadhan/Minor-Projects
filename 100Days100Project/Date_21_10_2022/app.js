// random value generated
var y = Math.floor(Math.random() * 99 + 1);
	console.log(y);
    
// counting the number of guesses
// made for correct Guess
var guess = 1;

document.getElementById("submitguess").onclick = function(){

// number guessed by user	
var x = document.getElementById("guessField").value;

if(x == y)
{	
("CONGRATULATIONS!!! YOU GUESSED IT RIGHT IN "
        + guess + " GUESS ");
}
else if(x > y) /* if guessed number is greater
            than actual number*/
{	
guess++;
alert("OOPS SORRY!! TRY A SMALLER NUMBER");
}
else
{
guess++;
alert("OOPS SORRY!! TRY A GREATER NUMBER")
}
}