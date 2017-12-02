<template>
<div>
<nav>
	<ul>
		<li><router-link :to="{ name:'home'}">Home</router-link></li>
		<li><router-link :to="{ name:'NutrientsInfo'}">Nutrients Information</router-link></li>
		<li><a>Walmart</a>
			<ul>
				<li><router-link :to="{ name:'walmartLocations'}">Locations</router-link></li>
				<li><a>Products</a>
					<ul>
						<li><router-link :to="{ name:'walmartProducts', params:{ catId:'1' }}">Bakery</router-link></li>
						<li><router-link :to="{ name:'walmartProducts', params:{ catId:'2' }}">Dairy</router-link></li>
						<li><router-link :to="{ name:'walmartProducts', params:{ catId:'3' }}">Seafood and Meat</router-link></li>
						<li><router-link :to="{ name:'walmartProducts', params:{ catId:'4' }}">Beer and Wine</router-link></li>
						<li><router-link :to="{ name:'walmartProducts', params:{ catId:'5' }}">Fruits and Vegetable</router-link></li>
					</ul>
				</li>
			</ul>
		</li>
		<li><a>Safeway</a>
			<ul>
				<li><router-link :to="{ name:'safewayLocations'}">Locations</router-link></li>
				<li><a>Products</a>
					<ul>
						<li><router-link :to="{ name:'safewayProducts', params:{ catId:'1' }}">Bakery</router-link></li>
						<li><router-link :to="{ name:'safewayProducts', params:{ catId:'2' }}">Dairy</router-link></li>
						<li><router-link :to="{ name:'safewayProducts', params:{ catId:'3' }}">Seafood and Meat</router-link></li>
						<li><router-link :to="{ name:'safewayProducts', params:{ catId:'4' }}">Beer and Wine</router-link></li>
						<li><router-link :to="{ name:'safewayProducts', params:{ catId:'5' }}">Fruits and Vegetable</router-link></li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
</nav>
</div>
</template>



<script>
export default {};
</script>

<style>
a { text-decoration: none; }
a:visited{
  color:#fff;
	text-decoration:none;
}
a:hover {
   text-decoration:none;
}
nav {
  text-align:center;
	color: #fff;
  width: 100%;
  background: #00802b;
  padding: 0;
  margin: 0;
  height: 60px;
  position:relative;
}

nav ul {
  background: #00802b;
	color: #fff;
  list-style:none;
  padding:0 20px;
  margin: 0;
  height: 60px;

}


nav ul li {
  display: inline-block;
}


nav ul li a {
  color:#00802b;
	color: #fff;
  display:block;
  padding:0px 40px;
  text-decoration:none;
  float: left;
  height: 60px;
   line-height: 60px;
}

nav ul li:hover {
  background: #0066cc;
}


nav ul li:hover > a{
    color:#FFFFFF;
}

nav ul li:hover > ul {
  display:block;
}

nav ul ul {
  background: #00802b;
  padding:0;
  text-align: center;
  display:none;
    width: 100%;
  position: absolute;
  top: 60px;
  left: 0px;
}

</style>
