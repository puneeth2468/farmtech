import streamlit as st

st.set_page_config(page_title="FarmTech Crop Information")

st.title("FarmTech Crop Information")

def get_crop_info(crop):
    crop_info = {
        "wheat": {
            "season": "Winter",
            "soil_conditions": "Well-drained loamy soil",
            "fertilizer_usage": "Nitrogen-rich fertilizers",
            "watering_needs": "Regular watering, avoid waterlogging",
            "common_pests": "Aphids, Hessian flies, Wheat midges"
        },
        "corn": {
            "season": "Summer",
            "soil_conditions": "Well-drained fertile soil",
            "fertilizer_usage": "Phosphorus and potassium-based fertilizers",
            "watering_needs": "Regular watering, especially during pollination",
            "common_pests": "Corn borers, Armyworms, Corn earworms"
        },
        "tomato": {
            "season": "Summer",
            "soil_conditions": "Well-drained sandy soil",
            "fertilizer_usage": "Balanced fertilizers with higher potassium content",
            "watering_needs": "Regular watering, avoid overwatering",
            "common_pests": "Aphids, Tomato hornworms, Whiteflies"
        },
        "potato": {
            "season": "Spring",
            "soil_conditions": "Loamy or sandy soil",
            "fertilizer_usage": "Fertilizers with higher phosphorus and potassium content",
            "watering_needs": "Regular watering, maintain soil moisture",
            "common_pests": "Colorado potato beetles, Aphids, Potato tuberworms"
        },
        "carrot": {
            "season": "Spring",
            "soil_conditions": "Well-drained sandy or loamy soil",
            "fertilizer_usage": "Fertilizers with higher phosphorus content",
            "watering_needs": "Regular watering, avoid excessive moisture",
            "common_pests": "Carrot rust flies, Carrot weevils, Aphids"
        },
        "paddy": {
            "season": "Monsoon",
            "soil_conditions": "Waterlogged paddy fields",
            "fertilizer_usage": "Fertilizers with balanced nitrogen, phosphorus, and potassium content",
            "watering_needs": "Maintain a consistent water level, avoid water stress",
            "common_pests": "Rice stem borers, Rice leaf folders, Rice hispa"
        },
        "chilies": {
            "season": "Summer",
            "soil_conditions": "Well-drained fertile soil",
            "fertilizer_usage": "Balanced fertilizers with higher nitrogen content",
            "watering_needs": "Regular watering, especially during fruiting",
            "common_pests": "Aphids, Pepper maggots, Pepper weevils"
        },
        "onions": {
            "season": "Cool season",
            "soil_conditions": "Well-drained sandy or loamy soil",
            "fertilizer_usage": "Fertilizers with higher phosphorus and potassium content",
            "watering_needs": "Moderate watering, avoid overwatering",
            "common_pests": "Onion thrips, Onion maggots, Leaf miners"
        },
        "cotton": {
            "season": "Summer",
            "soil_conditions": "Well-drained loamy soil",
            "fertilizer_usage": "Balanced fertilizers with higher nitrogen content",
            "watering_needs": "Moderate watering, avoid waterlogging",
            "common_pests": "Pink bollworm, whitefly attack"
        }
    }

    if crop in crop_info:
        return crop_info[crop]
    else:
        return None

crop_name = st.text_input("Enter the crop name:")

if crop_name:
    crop_info = get_crop_info(crop_name.lower())

    if crop_info:
        season = crop_info["season"]
        soil_conditions = crop_info["soil_conditions"]
        fertilizer_usage = crop_info["fertilizer_usage"]
        watering_needs = crop_info["watering_needs"]
        common_pests = crop_info["common_pests"]

        st.write(f"Season: {season}")
        st.write(f"Soil Conditions: {soil_conditions}")
        st.write(f"Fertilizer Usage: {fertilizer_usage}")
        st.write(f"Watering Needs: {watering_needs}")
        st.write(f"Common Pests: {common_pests}")
    else:
        st.write("Crop not found in the database.")
