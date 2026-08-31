<template>
    <div class="form-editing">
        <button @click="showForm = !showForm">
            Редагувати
        </button>
        <form v-if="showForm" @submit.prevent="editItem" class="edit-form">
            <input v-model="title" type="text" placeholder="Назва товару">
            <input v-model="image" type="text" placeholder="Назва фото">
            <textarea v-model="desc" placeholder="Опис товару"></textarea>
            <input v-model="price" type="number" placeholder="Ціна">
            
            <button type="submit">Зберегти</button>
        </form>
    </div>
</template>


<script>
import { ref } from 'vue'
import axios from 'axios'
export default {
    name: 'FormEdit',

    props: {
        item: Object
    },


    setup(props) {
        const showForm = ref(false)
        const title = ref(props.item.title)
        const image = ref(props.item.image)
        const desc = ref(props.item.desc)
        const price = ref(props.item.price)

        const editItem = async () => {
            try {
                await axios.put(
                    `http://127.0.0.1:8000/api/edit-item/${props.item.slug}`,
                    {
                        title: title.value,
                        image: image.value,
                        desc: desc.value,
                        price: price.value
                    }
                )

                window.location.reload()

            } catch (error) {
                console.log(error)
            }
        }
        return {
            showForm,
            title,
            image,
            desc,
            price,
            editItem
        }
    }
}
</script>

<style scoped>


.form-editing button {
    width: 100%;
    padding: 10px; 
    background-color: #1b4332;
    color: #ffffff; 
    border: none; 
    border-radius: 4px; 
    font-size: 14px; 
    font-weight: 500; 
    cursor: pointer; 
    transition: background-color 0.2s ease;
    margin-top: 15px;
    margin-bottom: 10px;
}

.form-editing button:hover {
    background-color: #143326; 
    transform: translateY(-5px);
}

.edit-form{
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.edit-form input,
.edit-form textarea{
    width: 100%;
    padding: 8px 10px;
    font-size: 14px;
    border: 1px solid #CCCCCC;
    border-radius: 4px;
    box-sizing: border-box;
    outline: none;
    background-color: #fafafa;
}

.edit-form input:focus,
.edit-form textarea:focus
{
    background-color: #ffffff;
    border-color: #1b4332;
}

.edit-form button{
    width: 100%;
    padding: 10px; 
    background-color: #1b4332;
    color: #ffffff; 
    border: none; 
    border-radius: 4px; 
    font-size: 14px; 
    font-weight: 500; 
    cursor: pointer; 
    transition: background-color 0.2s ease; 
}
.edit-form button:hover { 
    background-color: #143326; 
}
</style>