const FarmerButton = document.getElementById('FarmerButton');
const MiddleManButton = document.getElementById('MiddleManButton');
const main = document.getElementById('main');

FarmerButton.addEventListener('click', () => {
    main.classList.add("right-panel-active");
});
MiddleManButton.addEventListener('click', () => {
    main.classList.remove("right-panel-active");
});

