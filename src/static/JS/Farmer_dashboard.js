window.onscroll = function () { stickHeader() };
var header = document.getElementsByClassName("header")[0];
var sticky = header.offsetTop;
console.log(sticky);
function stickHeader() {
    if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}

// Show the selected section and hide the container
function showSection(sectionId) {
    const sectionToShow = document.getElementById(sectionId);
    sectionToShow.style.display = "block";
    sectionToShow.scrollIntoView({ behavior: "smooth", block: "start" });
    document.body.style.overflow = 'hidden';
}

// Go back to the top container and hide all sections
function goBack(sectionId) {
    const sectionToHide = document.getElementById(sectionId);
    sectionToHide.style.display = "none";
    document.getElementById("MainUpperContainer").style.display = "block";
    document.getElementById("header").scrollIntoView({ behavior: "smooth", block: "start" });
    document.body.style.overflow = 'auto';
}

let debtdetailbutton = document.getElementById("debtdetail")
debtdetailbutton.addEventListener('click', () => {
    console.log("Clicked");
    showSection("DebtDetailsSection");
})

let cropsalelbutton = document.getElementById("cropsale")
cropsalelbutton.addEventListener('click', () => {
    console.log("Clicked");
    showSection("CropsSoldSection");
})

let fertilizerborrowbutton = document.getElementById("fertilizerborrow")
fertilizerborrowbutton.addEventListener('click', () => {
    console.log("Clicked");
    showSection("FertilizerBorrowedSection");
})



let debtdetailBackButton = document.getElementById("debtdetailBackButton");
debtdetailBackButton.addEventListener('click', () => {
    console.log("Clicked");
    goBack("DebtDetailsSection");
})

let CropsSoldBackButton = document.getElementById("CropsSoldBackButton");
CropsSoldBackButton.addEventListener('click', () => {
    console.log("Clicked");
    goBack("CropsSoldSection");
})
let FertilizerBorrowedBackButton = document.getElementById("FertilizerBorrowedBackButton");
FertilizerBorrowedBackButton.addEventListener('click', () => {
    console.log("Clicked");
    goBack("FertilizerBorrowedSection");
})