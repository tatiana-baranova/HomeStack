
<script >

</script>

<template>
    <header>
        <img src="../../img/logo.svg" alt="">
        <ul>
            <li><a href="" class="active logo">Головна</a></li>
            <li><a href="" class="logo"></a>Товари</li>
            <li><a href="" class="logo"></a>Доставка</li>
            <li><a href="" class="logo"></a>Про нас</li>
            <li><img src="../../img/purchase.svg"></li>
        </ul>
    </header>

</template>



<style scoped>
header{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    margin-top: 30px;
}
header ul{
    list-style: none;
}
header ul li{
    display: inline-block;
    margin-left: 32px;
    cursor: pointer;
}
header ul li .active{
    padding: 5px 15px;
    background-color: #B2BAC1;
    border-radius: 20px;
}

header ul li .active:hover{
    color: white;
    background-color: #616364;
    
}
/* .logo {
    position: relative;
    bottom: 10px;
} */

</style>