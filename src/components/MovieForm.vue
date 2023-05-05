<template>
    <form @submit.prevent="saveMovie" id='movieForm' class="row g-3">

        <div v-if="response_type == 'success'" class="alert alert-success">
            {{ response.message }}
        </div>

        <div v-if="response_type == 'error'" class="alert alert-danger">
            <ul>
                <li v-for="error in response.errors">
                    {{ error }}
                </li>
            </ul>
        </div>

        <div class="form-group mb-3">
            <label for="title" class="form-label">Movie Title</label>
            <input type="text" name="title" class="formcontrol" />
        </div>

        <div class="form-group mb-3">
            <label for="desc" class="form-label">Movie Desciption</label>
            <textarea type="text" name="desc" class="formcontrol " />
        </div>

        <div>
            <label for="poster" class="form-label">Poster</label>
            <input type="file" name="poster" class="formcontrol" accept=".jpg, .jpeg, .png, .gif" />
        </div>

        <div>
            <input type="submit" value="Submit">
        </div>


    </form>
</template>

<style>
body {
    padding-top: 5rem;
}
</style>

<script setup>
import { ref, onMounted } from "vue"; onMounted(() => {
    getCsrfToken();
});
let csrf_token = ref("");
let response = ref([]);
let response_type = ref("");
function getCsrfToken() {
    fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
}
function saveMovie(){
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);
    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {       
            console.log(data);
            if (data.hasOwnProperty('errors')) {
                response.value = data;
                response_type.value = 'error';
            }
            else {
                response.value = data;
                response_type.value = 'success';
            }
        })
        .catch(function (error) {
            console.log(error, 'Error');
        });
}
</script>