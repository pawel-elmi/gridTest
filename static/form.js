// $(document).ready(function () {
//     $
// })


$(document).ready(function () {
    $("button").click(function () {
        httpGet();
    });

    

    // $("button").click(function () {
    //     $("#div1").load("demo_test.txt", function (responseTxt, statusTxt, xhr) {
    //         if (statusTxt == "success")
    //             alert("External content loaded successfully!");
    //         if (statusTxt == "error")
    //             alert("Error: " + xhr.status + ": " + xhr.statusText);
    //     });
    // });
});

function myFunction(){
    console.log("asdasd");
}

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}