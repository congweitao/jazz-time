import React from 'react';
import './App.css';
  
function App() {
    return (
        <div>
            <nav class="navbar background">
                <ul class="nav-list">
                    <div class="logo">
                        <img src="logo128.png" alt="" />
                    </div>
                    <li><a href="#MainPage">Home</a></li>
                    <li><a href="#3DMall">Products</a></li>
                    <li><a href="#Solutions">Solutions</a></li>
                    <li><a href='#Contact'>Company</a></li>
                </ul>
                <div class="rightNav">
                    <input type="text" name="search" id="search" />
                    <button class="btn btn-sm">Search</button>
                </div>
            </nav>
            <section class="section">
                <div class="box-main">
                    <div class="secondHalf">
	    		<br></br>
	    		<img src="image001.jpg" alt="p0"/>
                        <p class="text-small">
                            UNIWING is a technology company focused on industry, infrastructure, 
                            transport, and healthcare. From more resource-efficient factories, 
                            resilient supply chains, and smarter buildings and grids, to cleaner and more comfortable transportation 
                            as well as advanced healthcare, the company creates technology with purpose adding real value for customers. 
                            By combining the real and the digital worlds, UNIWING empowers its customers 
                            to transform their industries and markets, helping them to transform the everyday for billions of people. 
                        </p>
	    		<br></br>
	    		<br></br>
                    </div>
                </div>
            </section>
            <section class="sectioncontent">
                <div class="box-page">
                    <div class="secondHalf">
                        <h1 class="text-big" id="program">
                            Enhance digital transformation with customers and partners
                        </h1>
                        <p class="text-small">
                            Find or build IoT solutions to unite new or legacy machines and connect suppliers, 
                            customers, and a distributed workforce within a global ecosystem. 
                            UNIWING Industrial IoT is built around the principle that new solutions and data must 
                            interoperate through industry standards and prevent vendor lock-in. 
                            Achieve results at scale through faster discovery of assets, best-in-class global support, 
                            and years of security expertise built from the chip to the cloud.
                        </p>
	    		<br></br>
	    		<br></br>
                    </div>
                </div>
            </section>
            <section class="sectioncontent">
                <div class="box-page">
                    <div class="secondHalf">
                        <h1 class="text-big" id="program">
                            Share and embed 3D models anywhere online
                        </h1>
                        <p class="text-small">
                        Uniwing3D is a 3D modeling platform website to publish, share, discover, 
                        buy and sell 3D, VR and AR content. It provides a viewer based on the WebGL and WebXR technologies 
                        that allows users to display 3D models on the web, to be viewed on any mobile browser, desktop browser or Virtual Reality headset.
                        </p>
	    		<br></br>
	    		<br></br>
                    </div>
                </div>
            </section>
            <section class="sectioncontent">
                <div class="box-page">
                    <div class="secondHalf">
                        <h1 class="text-big" id="program">
                            Join millions of 3D creators
                        </h1>
                        <p class="text-small">
                            Uniwing3D is also a  3D content creation platform that supplies Job Offers for 3D Artists.
                            The platform has nearly endless demand for 3D assets. Every offer has a minimum category 
                            rank which the artist must have in order to apply for a job. The ranking was determined by 
                            the level of complexity of each model. Your rank however, is a result of the quality of your work.  
                            Sign up for Creators 3D for free and start GETTING PAID on your 3D creation abilities!
                        </p>
	    		<br></br>
	    		<br></br>
                    </div>
                </div>
            </section>
            <section class="sectioncontent">
                <div class="box-page">
                    <div class="secondHalf">
                        <h1 class="text-big" id="program">
                            Buy & sell 3D models on the Uniwing Store
                        </h1>
                        <p class="text-small">
                            UNIWING 3DExport is a marketplace where you can buy and sell 3D models, 3d print models and textures for using in CG projects.
                            Upload 3D Models, publish models and attract customers in the most efficient way possible and make your 3D assets profitable
                            by connecting you to an ever-increasing base of buyers from all over the globe.
                        </p>
	    		<br></br>
	    		<br></br>
                    </div>
                </div>
            </section>
            <footer className="footer">
                <p className="text-footer">
                    Copyright © 2022 Beijing UNIWING Tech. All rights are reserved
                </p>
            </footer>
        </div>
    )
}
  
export default App
