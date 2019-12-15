const chooseCosmeticsType = document.querySelector('select.cosmetics-filters-types');
const chooseCosmeticsTargetGender = document.querySelector('select.cosmetics-filters-target-gender');
const formSpace = document.querySelector('form div.cosmetics-chosen-filters');
const changeFormTemplate = () => {
  const cosmeticsType = chooseCosmeticsType.value;
  const cosmeticsTargetGender = chooseCosmeticsTargetGender.value;

  formSpace.innerHTML = cosmeticsMoreFilters[cosmeticsType];

  console.log(cosmeticsType, cosmeticsTargetGender);
};
chooseCosmeticsType.addEventListener('change', changeFormTemplate);
chooseCosmeticsTargetGender.addEventListener('change', changeFormTemplate);

const bodyCosmeticsFilters = `
    <div class="body-cosmetic-filters">
      <div>
	  	<span class="cosmetics-filters"><label class=filters-label>Skin type:</label></span>
 		<span class="cosmetics-filters"><label class=filters-label>Properties:</label></span>
      </div>
      <div>
      	<span class="cosmetics-filters">
	  		<select class="cosmetics-filters-skin-type">
	  			<option selected value="all">All</option>
				<option value="dehyderated" id="dehyderated">Dehyderated skin</option>
		        <option value="imperfections" id="imperfections">Imperfections</option>
		        <option value="inelastic" id="inelastic">Inelastic skin</option>
		        <option value="cellulite" id="cellulite">Cellulite</option>
		        <option value="sweating" id="sweating">Sweating skin</option>
		        <option value="sensitive" id="sensitive">Sensitive skin</option>
			</select> </span>

		<span class="cosmetics-filters">
			<select class="cosmetics-filters-properties">
			    <option selected value="all">All</option>
			    <option value="moisturizing">Moisturizing</option>
			    <option value="reviviscent">Reviviscent</option>
			    <option value="antiaging">Antiaging</option>
			    <option value="cleansing">Cleansing</option>
			    <option value="sunscreen">Sunscreen</option>
			</select></span>
      </div>

    </div>
`;

const faceCosmeticsFilters = `
    <div class="hair-cosmetic-filters">
     <div>
	  	<span class="cosmetics-filters"><label class=filters-label>Skin type:</label></span>
	  	<span class="cosmetics-filters"><label class=filters-label>Skin subtype:</label></span>
	  	<span class="cosmetics-filters"><label class=filters-label>Time of day:</label></span>
 		<span class="cosmetics-filters"><label class=filters-label>Properties:</label></span>
      </div>
      <div>
      	<span class="cosmetics-filters">
	  		<select class="cosmetics-filters-skin-type">
	  			<option selected value="all">All</option>
				<option value="dry">Dry</option>
		        <option value="normal">Normal</option>
		        <option value="oily">Oily</option>
		        <option value="combination">Combination</option>
			</select> </span>

		<span class="cosmetics-filters">
			<select class="cosmetics-filters-skin-subtype">
				<option selected value="all">All</option>
		        <option value="capillaries">Capillaries</option>
		        <option value="sensitive">Sensitive</option>
		        <option value="acne">Acne</option>
		        <option value="contaminated">Contaminated</option>
		        <option value="allergic">Allergic</option>
		        <option value="dehyderated">Dehyderated</option>
		        <option value="mature">Mature</option>
	      </select></span>

		<span class="cosmetics-filters">
			<select class="cosmetics-filters-time-of-day">
				<option selected value="all">All</option>
		        <option value="day">Day</option>
		        <option value="night">Night</option>
	      </select></span>

		<span class="cosmetics-filters">
			<select class="cosmetics-filters-properties">
			    <option selected value="all">All</option>
			    <option value="moisturizing">Moisturizing</option>
			    <option value="reviviscent">Reviviscent</option>
			    <option value="antiaging">Antiaging</option>
			    <option value="cleansing">Cleansing</option>
			    <option value="sunscreen">Sunscreen</option>
			</select></span>
      </div>

    </div>
`;

const hairCosmeticsFilters = `
    <div class="face-cosmetic-filters">
      <div>
	  	<span class="cosmetics-filters"><label class=filters-label>Hair type:</label></span>
	  	<span class="cosmetics-filters"><label class=filters-label>Hair problem:</label></span>
 		<span class="cosmetics-filters"><label class=filters-label>Properties:</label></span>
      </div>
      <div>
      	<span class="cosmetics-filters">
	  		<select class="cosmetics-filters-hair-type">
	  			<option selected value="all">All porosity</option>
				<option value="high-porosity">High porosity</option>
		        <option value="low-porosity">Low porosity</option>
		        <option value="medium-porosity">Medium porosity</option>
			</select> </span>

		<span class="cosmetics-filters">
	        <select class="cosmetics-filters-hair-problem">
	          <option selected value="all">All hair</option>
	          <option value="weak">Weak hair</option>
	          <option value="colored">Colored hair</option>
	          <option value="dandruff">Dandruff</option>
	          <option value="oily">Oily hair</option>
	        </select></span>

		<span class="cosmetics-filters">
			<select class="cosmetics-filters-properties">
			    <option selected value="all">All</option>
			    <option value="moisturizing">Moisturizing</option>
			    <option value="reviviscent">Reviviscent</option>
			    <option value="color-protection">Color protection</option>
			    <option value="against-hair-loss">Against hair loss</option>
			    <option value="against-dandruff">Against dandruff</option>
			    <option value="hair-growth">Hair growth</option>
			    <option value="smoothing">Smoothing</option>
			    <option value="against-greasiness">Against greasiness</option>
			</select></span>
      </div>

    </div>
`;



const handsFeetCosmeticsFilters = `
    <div class="handsFeet-cosmetic-filters">
      <div>
	  	<span class="cosmetics-filters"><label class=filters-label>Skin type:</label></span>
 		<span class="cosmetics-filters"><label class=filters-label>Properties:</label></span>
      </div>
      <div>
      	<span class="cosmetics-filters">
	  		<select class="cosmetics-filters-skin-type">
	  			<option selected value="all">All</option>
				<option value="dry">Dry</option>
		        <option value="normal">Normal</option>
		        <option value="dehyderated">Dehyderated</option>
		        <option value="inelastic">Inelastic</option>
			</select> </span>

		<span class="cosmetics-filters">
			<select class="cosmetics-filters-properties">
			    <option selected value="all">All</option>
			    <option value="moisturizing">Moisturizing</option>
			    <option value="reviviscent">Reviviscent</option>
			    <option value="sunscreen">Sunscreen</option>
			</select></span>
      </div>

    </div>
`;

const cosmeticsMoreFilters = {
  body: bodyCosmeticsFilters,
  hair: hairCosmeticsFilters,
  hands: handsFeetCosmeticsFilters,
  face: faceCosmeticsFilters,
  feet: handsFeetCosmeticsFilters,
};

const getCosmeticsFiltersData = () => {
	const cosmeticsType = chooseCosmeticsType.value;
 	const cosmeticsTargetGender = chooseCosmeticsTargetGender.value;
 	const cosmetic = document.querySelector('div.cosmetics');

	const commonCosmeticsData = {
    	cosmetic_type: cosmeticsType,
    	target_gender: cosmeticsTargetGender,
  	};

  	const bodyCosmeticData = () => {
    return (bodyHandsFeetCosmeticJson = {
      ...commonCosmeticsData,
      bodycosmetic__skin_type: cosmetic.querySelector('select.cosmetics-filters-skin-type').value,
      bodycosmetic__properties__name: cosmetic.querySelector('select.cosmetics-filters-properties').value,
      
    });
  };

  const handsFeetCosmeticData = () => {
    return (handsFeetCosmeticJson = {
      ...commonCosmeticsData,
      handscosmetic__skin_type: cosmetic.querySelector('select.cosmetics-filters-skin-type').value,
      handscosmetic__properties__name: cosmetic.querySelector('select.cosmetics-filters-properties').value,
      
    });
  };

  const faceCosmeticData = () => {
    return (faceCosmeticJson = {
      ...commonCosmeticsData,
      facecosmetic__skin_type: cosmetic.querySelector('select.cosmetics-filters-skin-type').value,
      facecosmetic__time_of_day: cosmetic.querySelector('select.cosmetics-filters-time-of-day').value,
      facecosmetic__skin_subtype: cosmetic.querySelector('select.cosmetics-filters-skin-subtype').value,
      facecosmetic__properties__name: cosmetic.querySelector('select.cosmetics-filters-properties').value,
    });
  };

  const hairCosmeticData = () => {
    return (hairCosmeticJson = {
      ...commonCosmeticsData,
	  haircosmetic__hair_type: cosmetic.querySelector('select.cosmetics-filters-hair-type').value,
	  haircosmetic__hair_problem: cosmetic.querySelector('select.cosmetics-filters-hair-problem').value,
      haircosmetic__properties__name: cosmetic.querySelector('select.cosmetics-filters-properties').value,
    });
  };

  if (cosmeticsType == 'body') {
    return bodyCosmeticData();
  } else if (cosmeticsType == 'face') {
    return faceCosmeticData();
  } else if (cosmeticsType == 'hair') {
    return hairCosmeticData();
  } else if (cosmeticsType == 'hands' || cosmeticsType == 'feet') {
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



const showFilteredCosmetics = response => {
  cosmetics = [];
  for (cosmeticPk in response) {
    cosmetics.push(`<li><a href="/cosmetic/show/${cosmeticPk}">${response[cosmeticPk]}</a></li>`)
  }
  return cosmetics.join('');
};
const changeCosmeticFilters = async () => {
  const jsonData = getCosmeticsFiltersData();
  const url = '/cosmetic/filter';
  const response = await requestPost(url, jsonData);
  const filteredCosmetics = showFilteredCosmetics(response);
  const cosmeticsList = document.querySelector('ul');
  cosmeticsList.innerHTML = filteredCosmetics;
};

const filterButton = document.querySelector('form button');
filterButton.addEventListener('click', changeCosmeticFilters);


