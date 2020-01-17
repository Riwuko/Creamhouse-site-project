var showIngredientButton = document.querySelector('input.add-next-ingredient');
var showSaveButton = document.querySelector('button.save-form');
showIngredientButton.style.display="none";
showSaveButton.style.display="none";

const chooseCosmeticType = document.querySelector('form select');
const formSpace = document.querySelector('form div.single-cosmetic');
const changeFormTemplate = () => {
  showIngredientButton.style.display = "block";
  showSaveButton.style.display = "block";
  const cosmeticType = chooseCosmeticType.value;
  formSpace.innerHTML = mainCosmeticForm;
  formSpace.innerHTML += partialCosmeticForm[cosmeticType];
  formSpace.innerHTML += cosmeticDescription;

  console.log(cosmeticType);
};
chooseCosmeticType.addEventListener('change', changeFormTemplate);

const mainCosmeticForm = `
  <div class="form-container">
    <div class="single-cosmetic-name">
        <div class="form-item">
      <label>Cosmetic Name: </label>
      <div class="alert"> <div class="cosmetic-name-alert"></div></div>
      <input type="text" name="cosmetic-name" />
    </div>
    </div>

    <div class="single-cosmetic-target-gender">
      <div class="form-item">
      <label>Target gender:</label>
        <div>
          <input type="radio" id="both" name="gender" checked>
          <label for="both">Both</label>
          <input type="radio" id="female" name="gender">
          <label for="female">Female</label>
          <input type="radio" id="male" name="gender">
          <label for="male">Male</label>
        </div>
    </div>
  </div>
`;

const cosmeticDescription = `
    <div class="single-cosmetic-description">
    <div class="form-item-area">
      <label>Description: </label>
      <textarea rows=10></textarea>
      </div>
    </div>
`;

const bodyCosmeticForm = `
    <div class="single-cosmetic-skin-type">
    <div class="form-item">
      <label>Cosmetic Skin Type:</label>
        <select class="single-cosmetic-skin-type">
        <option value="dehyderated" id="dehyderated">Dehyderated skin</option>
        <option value="imperfections" id="imperfections">Imperfections</option>
        <option value="inelastic" id="inelastic">Inelastic skin</option>
        <option value="cellulite" id="cellulite">Cellulite</option>
        <option value="sweating" id="sweating">Sweating skin</option>
        <option value="sensitive" id="sensitive">Sensitive skin</option>
      </select>
    </div>
    </div>

    <div class="single-cosmetic-properties">
    <div class="form-item">
      <legend>Choose cosmetic properties:</legend>
        <div>
          <input class="property" type="checkbox" id="moisturiing" name="property" value="moisturizing">
          <label for="moisturiing">Moisturizing</label>
        </div>
        <div>
          <input class="property" type="checkbox" id="reviviscent" name="property" value="reviviscent">
          <label for="reviviscent">Reviviscent</label>
        </div>
         <div>
          <input class="property" type="checkbox" id="antiaging" name="property" value="antiaging">
          <label for="antiaging">Antiaging</label>
        </div>
         <div>
          <input class="property" type="checkbox" id="cleansing" name="property" value="cleansing">
          <label for="cleansing">Cleansing</label>
        </div>
         <div>
          <input class="property" type="checkbox" id="sunscreen" name="property" value="sunscreen">
          <label for="sunscreen">Sunscreen</label>
        </div>
        </div>
    </div>
`;
const faceCosmeticForm = `
  <div class="form-container">
      <div class="single-cosmetic-time-of-day">
    <div class="form-item">
      <label>Time of day:</label>
        <div>
          <input type="radio" id="both" name="time-day">
          <label for="both">Both</label>
          <input type="radio" id="day" name="time-day">
          <label for="day">Day</label>
          <input type="radio" id="night" name="time-day">
          <label for="night">Night</label>
        </div>
      </div>
    </div>
    <div class="single-cosmetic-skin-type">  
    <div class="form-item-wide">
      <label>Cosmetic Skin Type: </label>
          <div>
            <input type="radio" id="dry" name="skin-type">
            <label for="dry">Dry</label>
            <input type="radio" id="normal" name="skin-type">
            <label for="normal">Normal</label>
            <input type="radio" id="oily" name="skin-type">
            <label for="oily">Oily</label>
            <input type="radio" id="combination" name="skin-type">
            <label for="combination">Combination</label>
          </div>
        </div>
    </div>
    </div>

    <div class="form-container">
    <div class = single-cosmetic-properties>
    <div class="form-item">
      <legend>Choose cosmetic properties:</legend>
        <div>
          <input class="property" type="checkbox" id="moisturiing" name="property" value="moisturizing"
          <label for="moisturiing">Moisturizing</label>
        </div>
        <div>
          <input class="property" type="checkbox" id="reviviscent" name="property" value="reviviscent">
          <label for="reviviscent">Reviviscent</label>
        </div>
         <div>
          <input class="property" type="checkbox" id="antiaging" name="property" value="antiaging">
          <label for="antiaging">Antiaging</label>
        </div>
         <div>
          <input class="property" type="checkbox" id="cleansing" name="property" value="cleansing">
          <label for="cleansing">Cleansing</label>
        </div>
         <div>
          <input class="property" type="checkbox" id="sunscreen" name="property" value="sunscreen">
          <label for="sunscreen">Sunscreen</label>
        </div> 
    </div>
    </div>
      <div class = "single-cosmetic-skin-subtype">
    <div class="form-item">
    <label>Cosmetic Skin Subtype: </label>
      <select class="single-cosmetic-skin-subtype">
        <option value="capillaries">Capillaries skin</option>
        <option value="sensitive">Sensitive skin</option>
        <option value="acne">Acne skin</option>
        <option value="contaminated">Contaminated skin</option>
        <option value="allergic">Allergic skin</option>
        <option value="dehyderated">Dehyderated skin</option>
        <option value="mature">Mature skin</option>
      </select>
    </div>
    </div>
    </div>
`;
const hairCosmeticForm = `
  <div class="form-container">
    <div class="single-cosmetic-hair-type">
      <div class="form-item">
      <label>Cosmetic hair type:</label>
        <div>
          <input type="radio" id="high-porosity" name="hair-type">
          <label for="high-porosity">High porosity</label>
        </div>
        <div>
          <input type="radio" id="low-porosity" name="hair-type">
          <label for="low-porosity">Low porosity</label>
        </div>
        <div>
          <input type="radio" id="medium-porosity" name="hair-type">
          <label for="medium-porosity">Medium-porosity</label>
        </div>
        <div>
          <input type="radio" id="all-porosity" name="hair-type">
          <label for="all-porosity">All porosity</label>
        </div>
    </div>
    </div>

    <div class="single-cosmetic-hair-problem">
        <div class="form-item">
      <label>Cosmetic hair problem:</label> 
        <select class="single-cosmetic-hair-problem">
          <option value="weak">Weak hair</option>
          <option value="colored">Colored hair</option>
          <option value="dandruff">Dandruff</option>
          <option value="oily">Oily hair</option>
          <option value="all-hair">All hair</option>
        </select>
        </div>
    </div>

    </div>

    <div class="single-cosmetic-properties">
      <div class="form-item-wide">
      <legend>Choose cosmetic properties:</legend>
      <div>
        <input class="property" type="checkbox" id="moisturizing" name="property" value="moisturizing"
        <label for="moisturizing">Moisturizing</label>

        <input class="property" type="checkbox" id="reviviscent" name="property" value="reviviscent">
        <label for="reviviscent">Reviviscent</label>

        <input class="property" type="checkbox" id="color-protection" name="property" value="color-protection">
        <label for="color-protection">Color protection</label>

        <input class="property" type="checkbox" id="against-hair-loss" name="property" value="against-hair-loss">
        <label for="against-hair-loss">Against hair loss</label>
      </div>
      <div>
        <input class="property" type="checkbox" id="against-dandruff" name="property" value="against-dandruff">
        <label for="against-dandruff">Against dandruff</label>

        <input class="property" type="checkbox" id="hair-growth" name="property" value="hair-growth">
        <label for="hair-growth">Hair growth</label>

        <input class="property" type="checkbox" id="smoothing" name="property" value="smoothing">
        <label for="smoothing">Smoothing</label>

      <input class="property" type="checkbox" id="against-greasiness" name="property" value="against-greasiness"
      <label for="against-greasiness">Against greasiness</label>
    </div>
    </div>
  </div>
`;

const handsFeetCosmeticForm = `
    <div class="single-cosmetic-skin-type"> 
    <div class="form-item-wide"> 
      <label>Cosmetic Skin Type:</label>
          <div>
            <input type="radio" id="dry" name="skin-type">
            <label for="dry">Dry</label>
            <input type="radio" id="normal" name="skin-type">
            <label for="dry">Normal</label>
            <input type="radio" id="dehyderated" name="skin-type">
            <label for="dehyderated">Dehyderated</label>
            <input type="radio" id="inelastic" name="skin-type">
            <label for="inelastic">Inelastic</label>
          </div>
          </div>
    </div>

    <div class="single-cosmetic-properties" name="single-cosmetic-propeties">
    <div class="form-item">
      <legend>Choose cosmetic properties:</legend>
        <div>
          <input class="property" type="checkbox" id="moisturizing" name="property" value="moisturizing"
          <label for="moisturizing">Moisturizing</label>
        </div>
        <div>
          <input class="property" type="checkbox" id="reviviscent" name="property" value="reviviscent">
          <label for="reviviscent">Reviviscent</label>
        </div>
         <div>
          <input class="property" type="checkbox" id="sunscreen" name="property" value="sunscreen">
          <label for="sunscreen">Sunscreen</label>
        </div>
        </div>
    </div>
 `;

const partialCosmeticForm = {
  body: bodyCosmeticForm,
  hair: hairCosmeticForm,
  hands: handsFeetCosmeticForm,
  face: faceCosmeticForm,
  feet: handsFeetCosmeticForm,
};

const changeSuggestions = async ingredientId => {
  const inputElement = document.querySelector(`div#${ingredientId} input`);
  const inputValue = inputElement.value;
  const { ingredients } = await requestGet('/ingredient/check/name', `ingredient=${inputValue}`);
  const ingredientElement = inputElement.parentElement;
  const suggestionList = ingredientElement.querySelector('ul.suggestions');
  const suggestions = [];
  ingredients.forEach(e => suggestions.push(`<li>${e}</li>`));
  suggestionList.innerHTML = suggestions.join('');
};

window.ingredientId = 1;
const addNextIngredient = ingredientElement => {
  const newIngredient = `
        <div class="new-ingredient">
        <div class="form-item-font-black">
        <span class="extra-white-element"><label for="name">Add ingredient:</label></span>
        <input type="text" name="ingredient-name" autocomplete="off">
        <ul class="suggestions"></ul>
        </div>`;
  const div = document.createElement('div');
  div.classList.add('next-cosmetic-ingredient');
  const ingredientId = `ingredient${window.ingredientId}`;
  div.setAttribute('id', ingredientId);
  div.innerHTML = newIngredient;
  ingredientElement.appendChild(div);
  ingredientInput = document.querySelector(`div#${ingredientId} input`);
  ingredientInput.addEventListener('input', () => {
    changeSuggestions(ingredientId);
  });
  window.ingredientId += 1;
};
document
  .querySelector('input.add-next-ingredient')
  .addEventListener('click', () => {
    addNextIngredient(document.querySelector('div.single-cosmetic'));
  });

const getCosmeticData = () => {
  const cosmeticType = document.querySelector('form select').value;
  const cosmetic = document.querySelector('div.single-cosmetic');
  const cosmeticIngredients = [];
  for (input of document.querySelectorAll(
    'div.next-cosmetic-ingredient input',
  )) {
    cosmeticIngredients.push(input.value);
  }
  const cosmeticProperties = [];
  for (input of cosmetic.querySelectorAll('.property:checked')) {
    cosmeticProperties.push(input.value);
  }

  const commonCosmeticData = {
    cosmetic_type: cosmeticType,
    name: cosmetic.querySelector('div.single-cosmetic-name input').value,
    description: cosmetic.querySelector(
      'div.single-cosmetic-description textarea',
    ).value,
    target_gender: cosmetic.querySelector(
      'div.single-cosmetic-target-gender input:checked',
    ).id,
    ingredients: cosmeticIngredients,
  };

  const bodyCosmeticData = () => {
    return (bodyHandsFeetCosmeticJson = {
      ...commonCosmeticData,
      skin_type: cosmetic.querySelector('div.single-cosmetic-skin-type select')
        .value,
      properties: cosmeticProperties,
    });
  };

  const handsFeetCosmeticData = () => {
    return (handsFeetCosmeticJson = {
      ...commonCosmeticData,
      skin_type: cosmetic.querySelector(
        'div.single-cosmetic-skin-type input:checked',
      ).id,
      properties: cosmeticProperties,
    });
  };

  const faceCosmeticData = () => {
    return (faceCosmeticJson = {
      ...commonCosmeticData,
      skin_type: cosmetic.querySelector(
        'div.single-cosmetic-skin-type input:checked',
      ).id,
      skin_subtype: cosmetic.querySelector(
        'div.single-cosmetic-skin-subtype select',
      ).value,
      time_of_day: cosmetic.querySelector(
        'div.single-cosmetic-time-of-day input:checked',
      ).id,
      properties: cosmeticProperties,
    });
  };

  const hairCosmeticData = () => {
    return (hairCosmeticJson = {
      ...commonCosmeticData,
      hair_type: cosmetic.querySelector(
        'div.single-cosmetic-hair-type input:checked',
      ).id,
      hair_problem: cosmetic.querySelector(
        'div.single-cosmetic-hair-problem select',
      ).value,
      properties: cosmeticProperties,
    });
  };

  if (cosmeticType == 'body') {
    return bodyCosmeticData();
  } else if (cosmeticType == 'face') {
    return faceCosmeticData();
  } else if (cosmeticType == 'hair') {
    return hairCosmeticData();
  } else if (cosmeticType == 'hands' || cosmeticType == 'feet') {
    return handsFeetCosmeticData();
  }
};

const checkCompability= (name,element,regex,alert) => {
  const correct=regex.test(element);
  const stringPath = 'form div.cosmetic-'.concat(name).concat('-alert'); 
  const formSpace = document.querySelector(stringPath);
  if(!correct){
    formSpace.innerHTML = alert;
    return false;
  }
  formSpace.innerHTML = "";
  return true;
};

const initialValidate = () => {
  var correct=true;
  const jsonData = getCosmeticData();
  const name =  jsonData['name'];
  var regex = /.{3,50}/;
  if(!checkCompability("name",name,regex,"Enter correct name (between 3 and 50 characters)")){
    correct = false;
  }

  return correct;
};

const addCosmetic = async () => {
  if(initialValidate()){
  const jsonData = getCosmeticData();
  console.log(jsonData);
  resp = await requestPost(`/cosmetic/add/${jsonData['cosmetic_type']}`, jsonData);
  console.log(resp);
  window.location.replace('/success')
}
};

document.querySelector('form button').addEventListener('click', addCosmetic);
