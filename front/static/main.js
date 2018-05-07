$(function() {
    $('#white').on('click', handleWhiteClick)
    $('#black').on('click', handleBlackClick)

    // hide color hex value and guesses
    $('.message').hide()
    $('.circle').hide()

    $('#showColorIdCheckbox').on('change', handleShowColorCheckboxClick)

    getNewColors()
});


function getNewColors() {
    $.ajax({
        url: "/json/color.get",
        type: "get",
        success: setColors
    });
}

function setColors(input) {
    $('#container').css({"background": input["color"]})

    $(".message").text(input["color"])

    $('#iteration').text(input["iteration"])
    $('#prob-white').text(input["white_probability"])
    $('#prob-black').text(input["black_probability"])
    if (input["guess"] === "white") {
        $("#guess-white").show()
        $("#guess-black").hide()
    } else {
        $("#guess-white").hide()
        $("#guess-black").show()
    }
}

function _handleClick(label) {
    input = $('#container').css("background-color")
    $.ajax({
        url: "/json/color.pick",
        type: "post",
        data: JSON.stringify({pick: label, color: input}),
        contentType: 'application/json',
        success: getNewColors
    });
}

function handleWhiteClick() {
    _handleClick("white")
}

function handleBlackClick() {
    _handleClick("black")
}

function handleShowColorCheckboxClick() {
    if ($(this).is(':checked')) {
        $('.message').show();
    } else {
        $('.message').hide();
    }
}
