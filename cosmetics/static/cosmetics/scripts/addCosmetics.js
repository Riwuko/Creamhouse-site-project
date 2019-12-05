const chooseCosmeticType = document.querySelector('form select');
const formSpace = document.querySelector('form div.single-cosmetic');
const changeFormTemplate = () => {
    const cosmeticType = chooseCosmeticType.value;
    formSpace.innerHTML = mainCosmeticForm;
    formSpace.innerHTML += partialCosmeticForm[cosmeticType];
    console.log(cosmeticType);
};
chooseCosmeticType.addEventListener('change', changeFormTemplate);



const mainCosmeticForm = `
    <div class="single-cosmetic-name">
      <label>Cosmetic Name:</label>
      <input type="text" name="cosmetic-name" />
    </div>
    <div class="single-cosmetic-target-gender">
      <label>Target gender:</label>
  <select>
    <option selected disabled hidden>Choose Target Gender</option>
    <option value="male">Male</option>
    <option value="female">Female</option>
    <option value="both">Both</option>
  </select>
`;

const bodyCosmeticForm = `
    <div class="single-cosmetic-skin-type">
      <label>Cosmetic Skin Type:</label>
      <input type="text" name="cosmetic-skin-type" />
    </div>
  <select class="single-cosmetic-property">
    <option selected disabled hidden>Choose Property</option>
    <option value="male">Male</option>
    <option value="female">Female</option>
    <option value="both">Both</option>
  </select>  
`
const partialCosmeticForm = {
   body: bodyCosmeticForm,
   hair: '',
   hands: '',
   face: '',
   feet: '',
};
