$(document).ready(function(){
    var numRows = 1;
    var maxRows = 9;
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
            newrow.getElementsByTagName("select")[1].setAttribute("name", "salt-tolerance-input-" + numRows.toString());
            newrow.getElementsByTagName("select")[2].setAttribute("name", "drought-tolerance-input-" + numRows.toString());
            newrow.getElementsByTagName("input")[1].setAttribute("name", "min-spread-input-" + numRows.toString());
            newrow.getElementsByTagName("input")[2].setAttribute("name", "min-height-input-" + numRows.toString());
            newrow.getElementsByTagName("input")[3].setAttribute("name", "min-roots-input-" + numRows.toString());
            var months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"];
            for(var i = 0; i < 12; i ++)
            {
                newrow.getElementsByTagName("input")[4 + i].setAttribute("name", "blooms-in-" + months[i] + "-input-" + numRows.toString());
            }
            delbutton.classList.remove("hidden");
            delbutton.childNodes[1].id = "del-btn-" + numRows.toString();
            newrow.getElementsByTagName("div")[0].appendChild(delbutton);
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
        $("#number-input-3").attr('id', 'wtf');
        for(var i = numClickedOn + 1; i <= numRows; i++)
        {
            $("#input-group-" + i.toString()).attr('id', "input-group-" + (i - 1).toString());
            $("#del-btn-" + i.toString()).attr('id', "del-btn-" + (i - 1).toString());
            $("[name = 'number-input-" + i.toString() + "']").attr('name', "number-input-" + (i - 1).toString());
            $("[name = 'type-input-" + i.toString() + "']").attr('name',"type-input-" + (i - 1).toString());
            $("[name = 'salt-tolerance-input-" + i.toString() + "']").attr('name',"salt-tolerance-input-" + (i - 1).toString());
            $("[name = 'drought-tolerance-input-" + i.toString() + "']").attr('name',"drought-tolerance-input-" + (i - 1).toString());
            $("[name = 'min-spread-input-" + i.toString() + "']").attr('name', "min-spread-input-" + (i - 1).toString());
            $("[name = 'min-height-input-" + i.toString() + "']").attr('name',"min-height-input-" + (i - 1).toString());
            $("[name = 'min-roots-input-" + i.toString() + "']").attr('name',"min-roots-input-" + (i - 1).toString());
            var months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"];
            for(var j = 0; j < 12; j ++)
            {
                $("[name = 'blooms-in" + months[i] + "-input-" + i.toString() + "']").attr('name',"blooms-in-" + months[i] + "-input-" + (i - 1).toString());
            }

        }
        numRows --;
        document.getElementById("numRows").setAttribute("value", numRows.toString());

        $("#" + "input-group-" + numClickedOn.toString()).animate({"margin-left" : "+=1000"}, function(){
            $("#" + "input-group-" + numClickedOn.toString()).remove();
        });
    });
});

function getIDNumberFromString(string, numLetters)
{
    return parseInt(string.substring(numLetters, string.length));
}
