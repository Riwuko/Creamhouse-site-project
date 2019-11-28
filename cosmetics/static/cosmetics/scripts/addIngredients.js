const addRelatedName = (ingredientElement) => {
  console.log('asdasd')
  const newRelatedName = `
    <div class="single-ingredient-name">
        <label for="name">Related Name:</label>
        <input type="text" name="ingredient-name">
    </div>`;
  ingredientElement.innerHTML += newRelatedName;
};

document.querySelector('input.add-related-name').addEventListener("click", () => {addRelatedName(document.querySelector('div.single-ingredient'))});