window.onload = function(){

    let item1 = document.getElementById('checkbox1');
    let item2 = document.getElementById('checkbox2');
    let item3 = document.getElementById('checkbox3');

    let pic1 = document.getElementById('checkbox4');
    let pic2 = document.getElementById('checkbox5');
    let pic3 = document.getElementById('checkbox6');
    let pic4 = document.getElementById('checkbox7');

    let checkbox1 = document.getElementById('checkbox-1');
    let checkbox2 = document.getElementById('checkbox-2');
    let checkbox3 = document.getElementById('checkbox-3');

    item1.onclick = () => {
        item1.checked = true;
        item2.checked = false;
        item3.checked = false;
    }

    item2.onclick = () => {
        item2.checked = true;
        item1.checked = false;
        item3.checked = false;
    }

    item3.onclick = () => {
        item3.checked = true;
        item1.checked = false;
        item2.checked = false;
    }

    pic1.onclick = () => {
        pic1.checked = true;
        pic2.checked = false;
        pic3.checked = false;
        pic4.checked = false;
    }

    pic2.onclick = () => {
        pic2.checked = true;
        pic1.checked = false;
        pic3.checked = false;
        pic4.checked = false;
    }

    pic3.onclick = () => {
        pic3.checked = true;
        pic1.checked = false;
        pic2.checked = false;
        pic4.checked = false;
    }

    pic4.onclick = () => {
        pic4.checked = true;
        pic1.checked = false;
        pic2.checked = false;
        pic3.checked = false;
    }
    
    
    checkbox1.checked = true;
    document.getElementById("generate-1").value = "Spring packing list - Get $10 shorts and skirts NOW!";
    document.getElementById("generate-2").value = "Your spring break will be brighter than your ex's future!";
    document.getElementById("generate-3").value = "Leave your prints in the sand! Shop our latest tops!";

    checkbox1.onclick = () => {
        console.log("Checkbox 1 has been clicked");
        document.getElementById("generate-1").value = "Spring packing list - Get $10 shorts and skirts NOW!";
        document.getElementById("generate-2").value = "Your spring break will be brighter than your ex's future!";
        document.getElementById("generate-3").value = "Leave your prints in the sand! Shop our latest tops!";
        checkbox1.setAttribute("checked", "true");
        checkbox2.checked = false;
        checkbox3.checked = false;
    };

    checkbox2.onclick = () => {
        console.log("Checkbox 2 has been clicked");
        document.getElementById("generate-1").value = "Searching for sun!";
        document.getElementById("generate-2").value = "Sunny state of mind!";
        document.getElementById("generate-3").value = "Surf, Sand, and Sun!";
        checkbox1.checked = false;
        checkbox2.setAttribute("checked", "true");
        checkbox3.checked = false;
    };

    checkbox3.onclick = () => {
        console.log("Checkbox 3 has been clicked");
        document.getElementById("generate-1").value = "Checkbox 3 has been selected";
        document.getElementById("generate-2").value = "Checkbox 3 has been selected";
        document.getElementById("generate-3").value = "Checkbox 3 has been selected";
        checkbox1.checked = false;
        checkbox2.checked = false;
        checkbox3.setAttribute("checked", "true");
    };
};