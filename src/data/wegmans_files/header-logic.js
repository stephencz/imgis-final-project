// Wrap in IIFE to execute immediately & avoid polluting global namespace
// pulled from header.php Unata shared header section
// 1014

//function setHomeURLs(wegmansHome="#", UAThome="#", hdrServiceReady=null) {
function setHomeURLs(wegmansHome, UAThome, hdrServiceReady) {

    if ( !hdrServiceReady || (hdrServiceReady == null )) {
        return; // NOP
    }
    if ( !wegmansHome ) {
        wegmansHome = "#";
    }
    if ( !UAThome ) {
        UAThome = "#";
    }
    // (Initialize UnataComm hdrServiceReady done in header.php)

    // WPsiteRoot & UATshopRoot are set in header.php -- the site root and platform shop root domain names
    // Alternatively, these values could be stored in the wordpress database/PHP variables.
    WPsiteRoot = wegmansHome; // e.g.,"https://staging2.wegmans.com/";
    UATshopRoot = UAThome;    // e.g., "https://shop-uat.wegmans.com/";

    // Config for initialization.
    // Handle Case 1 & 2 by default: shop platform mobile-web and staging2 mobile-web
    // Should point to WP site root. 
    var homeLink = WPsiteRoot;

    // Initialize the header on platform.
    // Note: This event only fires on platform once header has been fully loaded has been dispatched.
    hdrServiceReady.listen('unata-header-loaded', function() {
        updateHomeLinks(homeLink)
    });

    // On Staging2, initialize the header when the mobile-service-ready event has fired.
    // Handle 3: in-app browser
    // Should point to platform/native app root.
    hdrServiceReady.listen('unata-mobile-service-ready', function() {
        // Handle  mobile-web as an override.
        // If there is no flag in localstorage, we are in  mobile web.
        if (!!localStorage.getItem("una_in_app_browser")) { // need double negative to get boolean
            homeLink = UATshopRoot;
        }
        updateHomeLinks(homeLink);
    });

    /**
     * Updates the house and logo home links
     * @param {string} newUrl - the new url to set home links to
     */
    function updateHomeLinks(newUrl) {
        // set mobile house image's link / home page
        if (document.getElementById('houseLinkedImage')) {
            console.log(" * house: " + newUrl);
            document.getElementById('houseLinkedImage').href = newUrl;
        }
        // set mobile logo's link / home page
        if (document.getElementById('logoLinkedImage')) {
            console.log(" * logo: " + newUrl);
            document.getElementById('logoLinkedImage').href = newUrl;
        }
    }
};