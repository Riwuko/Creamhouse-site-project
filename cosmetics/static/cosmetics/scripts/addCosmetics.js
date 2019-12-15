const chooseCosmeticType = document.querySelector('form select');
const formSpace = document.querySelector('form div.single-cosmetic');
const changeFormTemplate = () => {
  const cosmeticType = chooseCosmeticType.value;
  formSpace.innerHTML = mainCosmeticForm;
  formSpace.innerHTML += partialCosmeticForm[cosmeticType];
  formSpace.innerHTML += cosmeticDescription;

  console.log(cosmeticType);
};
chooseCosmeticType.addEventListener('change', changeFormTemplate);

const mainCosmeticForm = `
    <div class="single-cosmetic-name">
      <label>Cosmetic Name: </label>
      <input type="text" name="cosmetic-name" />
    </div>
    <div class="single-cosmetic-target-gender">
      <label>Target gender:</label>
        <div>
          <input type="radio" id="both" name="gender" checked>
          <label for="both">Both</label>
          <input type="radio" id="female" name="gender">
          <label for="female">Female</label>
          <input type="radio" id="male" name="gender">
          <label for="male">Male</label>
        </div>
`;

const cosmeticDescription = `
    <div class="single-cosmetic-description">
      <label>Description: </label>
      <textarea></textarea>
    </div>
`;

const bodyCosmeticForm = `
    <div class="single-cosmetic-skin-type">
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

    <div class="single-cosmetic-properties">
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
`;
const faceCosmeticForm = `
    <div class="single-cosmetic-skin-type">  
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

    <div class = "single-cosmetic-skin-subtype">
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

    <div class="single-cosmetic-time-of-day">
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

    <div class = single-cosmetic-properties>
      <legend>Choose cosmetic properties:</legend>
        <div>
          <input class="property" type="checkbox" id="moisturiing" name="property" value="moisturizing"
          <label for="moisturiing">Moisturizing</label>
        </div>
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
`;
const hairCosmeticForm = `
    <div class="single-cosmetic-hair-type">
      <label>Cosmetic hair Type:</label>
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

    <div class="single-cosmetic-hair-problem">
      <label>Cosmetic hair problem:</label> 
        <select class="single-cosmetic-hair-problem">
          <option value="weak">Weak hair</option>
          <option value="colored">Colored hair</option>
          <option value="dandruff">Dandruff</option>
          <option value="oily">Oily hair</option>
          <option value="all-hair">All hair</option>
        </select>
    </div>

    <div class="single-cosmetic-properties">
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
`;

const handsFeetCosmeticForm = `
    <div class="single-cosmetic-skin-type">  
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

    <div class="single-cosmetic-properties" name="single-cosmetic-propeties">
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
 `;

const partialCosmeticForm = {
  body: bodyCosmeticForm,
  hair: hairCosmeticForm,
  hands: handsFeetCosmeticForm,
  face: faceCosmeticForm,
  feet: handsFeetCosmeticForm,
};

const addNextIngredient = ingredientElement => {
  const newIngredient = `
        <div class="new-ingredient">
        <label for="name">Add ingredient:</label>
        <input type="text" name="ingredient-name">
        <ul></ul>
        </div>`;
  const div = document.createElement('div');
  div.classList.add('next-cosmetic-ingredient');
  div.innerHTML = newIngredient;
  ingredientElement.appendChild(div);
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
    type: cosmeticType,
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
      commonCosmeticData,
      skin_type: cosmetic.querySelector('div.single-cosmetic-skin-type select')
        .value,
      properties: cosmeticProperties,
    });
  };

  const handsFeetCosmeticData = () => {
    return (handsFeetCosmeticJson = {
      commonCosmeticData,
      skin_type: cosmetic.querySelector(
        'div.single-cosmetic-skin-type input:checked',
      ).id,
      properties: cosmeticProperties,
    });
  };

  const faceCosmeticData = () => {
    return (faceCosmeticJson = {
      commonCosmeticData,
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
      commonCosmeticData,
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

const requestPost = async (url, jsonData) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': Cookies.get('csrftoken'),
    },
    body: JSON.stringify(jsonData),
    credentials: 'include',
  });
  return response.json();
};

const addCosmetic = async () => {
  const jsonData = getCosmeticData();
  console.log(jsonData);
  resp = await requestPost('/cosmetic/add', jsonData);
  console.log(resp);
  // window.location.replace('/')
};

document.querySelector('form button').addEventListener('click', addCosmetic);
