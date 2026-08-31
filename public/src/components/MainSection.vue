<template>
    <div class="wrapper">
        <img src="../../img/main.svg" alt="">
        <div>
            <img src="../../img/star.svg" alt="">
            <h1>Shop</h1>
            <h2>online</h2>
            <h3>now</h3>
            <p>Знаходьте потрібні товари легко та швидко. Обирайте серед актуального асортименту, оформлюйте замовлення онлайн та отримуйте покупки зручно й без зайвих турбот.</p>
            <button>Розпочати покупки</button>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style scoped>
.wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 150px 0;
}

.wrapper > div {
    margin-left: 150px;
    color: #373845;
}

.wrapper > div h1 {
    font-weight: 400;
    font-size: 90px;
}

.wrapper > div h2, .wrapper > div h3 {
    font-weight: 400;
    font-size: 70px;
}

.wrapper > div h3 {color: #5CDDBC;}

.wrapper > div p {
    font-size: 18px;
    width: 500px;
    margin: 20px 0;
}

.wrapper > div button {
    font-weight: 600;
    font-size: 18px;
    color: #2F323A;
    background: #5CDDBC;
    border-radius: 25px;
    border: 0;
    padding: 15px 25px;
    cursor: pointer;
}

.wrapper > div button:hover {
    transform: translateY(-5px);
}
</style>