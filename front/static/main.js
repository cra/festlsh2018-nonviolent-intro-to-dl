var whiteBlock = document.getElementById("white")
var blackBlock = document.getElementById("black")
var iterationText = document.getElementById("iteration")

$(function() {
    getNewColors()

    $("#white").on('click', handleWhiteClick)
    $("#black").on('click', handleBlackClick)
});


function getNewColors() {
    $.ajax({
        url: "/json/color.get",
        type: "get",
        success: setColors
    });
}

function setColors(input) {
    $(whiteBlock).css({"background": input["white"]})
    $("#white > .message").text(input["white"])

    $(blackBlock).css({"background": input["black"]})
    $("#black> .message").text(input["black"])

    $(iterationText).text(input["iteration"])
}

function _handleClick(label, input) {
    $.ajax({
        url: "/json/color.pick",
        type: "post",
        data: JSON.stringify({pick: label, color: input}),
        contentType: 'application/json',
        success: getNewColors
    });
}

function handleWhiteClick() {
    color = $(whiteBlock).css("background-color")
    _handleClick("white", color)
}

function handleBlackClick() {
    color = $(blackBlock).css("background-color")
    _handleClick("black", color)
}
