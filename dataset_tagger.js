function like(){
	console.log(...$('*[data-testid="recsSmartImage#0"]').style.backgroundImage)
	console.log(1)
}

function dislike(){
	console.log(...$('*[data-testid="recsSmartImage#0"]').style.backgroundImage)
    console.log(0)
}

$('*[data-testid="gamepadDislike"]').addEventListener("click",dislike)
$('*[data-testid="gamepadLike"]').addEventListener("click",like)