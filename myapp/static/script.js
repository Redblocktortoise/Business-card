function getProducts(response) {
    var Json = JSON.parse(response)
    textlist = ""
    for (var i = 0; i < Json.length; i++) {
        textlist += "<input type='radio'  name='product' id=" + Json[i].pk + ">" + Json[i].fields['name'] + ", €" + Json[i].fields['price'] + "<br>"
    }
    $('#name').val('Name')
    $('#description').val("Description")
    $('#price').html("Price")
    if (textlist == "")
        $("#productlist").html("No products available, add one below please")
    else
        $("#productlist").html(textlist)

}