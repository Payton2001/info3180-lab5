<template>
    <div class="page-header">
        <h2>Movies</h2>
    </div>


    <div class="movie-container">

        <div class="card movie-card" v-for="movie in movies">

            <div class="movie-image">
                <img class="movie-img" v-bind:src="movie.poster" alt="movie poster" />
            </div>

            <div class="movie-body">
                <h3 class="card-title">{{ movie.title }}</h3>
                <p class="card-text">{{ movie.description }}</p>
            </div>
        </div>
    </div>
</template>

<style>
.page-header {
    text-align: center;
    margin-bottom: 20px;
}

.movie-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    column-gap: 10px;
    padding: 15px;
}

.movie-card {
    display: flex;
    flex-direction: row;
    column-gap: 10px;
    width: calc(33.33% - 10px);
    margin-bottom: 20px;
    box-sizing: border-box;

}

.movie-image {
    display: flex;
    align-items: flex-start;
    width: 50%;
}

.movie-img {
    width: 100%;
    height: auto;
}

@media screen and (max-width: 800px) {
    .movie-card {
        width: 100%;
    }
}
</style>

<script setup>
import { ref, onMounted } from "vue"; onMounted(() => {
    fetchMovies();
});
let movies = ref([]);
const fetchMovies = () => {
    fetch('/api/v1/movies')
        .then((response) =>
            response.json())

        .then((data) => {
            console.log(data);
            movies.value = data.movies;
        })
}
</script>