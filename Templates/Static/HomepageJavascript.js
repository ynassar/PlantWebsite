$(document).ready(function(){
    var numRows = 1;
    var maxRows = 10;
    $(document).on("click", ".addbtn", function(event){
        if(numRows < maxRows)
        {
            numRows ++;
            var row = document.getElementById("input-group-1");
            var newrow = row.cloneNode(true);
            var delbutton = document.getElementById("delbutton").cloneNode(true);
            newrow.id = "input-group-" + numRows.toString();
            newrow.getElementsByTagName("input")[0].setAttribute("name", "number-input-" + numRows.toString());
            newrow.getElementsByTagName("select")[0].setAttribute("name", "type-input-" + numRows.toString());
            delbutton.classList.remove("hidden");
            delbutton.childNodes[1].id = "del-btn-" + numRows.toString();
            newrow.appendChild(delbutton);
            var form = document.getElementById("number-type-inputform");
            form.appendChild(newrow);
            document.getElementById("numRows").setAttribute("value", numRows.toString());
        }
        else
        {

        }
    });
    $(document).on("click", ".removebtn", function(event){
        var numClickedOn = getIDNumberFromString(event.target.id, 8);
        var form = document.getElementById("number-type-inputform");

        $("#" + "input-group-" + numClickedOn.toString()).fadeOut(1000, function() {
           $(this).remove();
        });
        //form.removeChild(document.getElementById("input-group-" + numClickedOn.toString()));
        for(var i = numClickedOn + 1; i <= numRows; i++)
        {
            document.getElementById("input-group-" + i.toString()).id = "input-group-" + (i - 1).toString();
            document.getElementById("del-btn-" + i.toString()).id = "del-btn-" + (i - 1).toString();
        }
        numRows --;
        document.getElementById("numRows").setAttribute("value", numRows.toString());
    });
});

function getIDNumberFromString(string, numLetters)
{
    return parseInt(string.substring(numLetters, string.length));
}
