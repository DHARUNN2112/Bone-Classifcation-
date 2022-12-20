double getEccentricity(Moments &mu){
    double bigSqrt = sqrt( ( mu.m20 - mu.m02 ) *  ( mu.m20 - mu.m02 )  + 4 * mu.m11 * mu.m11  );
    return (double) ( mu.m20 + mu.m02 + bigSqrt ) / ( mu.m20 + mu.m02 - bigSqrt );
}
void tryElongation(){
    Mat img;
    img = imread("D:\DHARUN\STUDY\SEM 5\Research\Dicom Sample\hand-x-ray-768x923.jpg");
    cvtColor(img, img, CV_RGB2GRAY);
    close( &img );
    imshow( "img", img );
    RNG rng(12345);
    Mat drawing = Mat::zeros( img.size(), CV_8UC3 );
    vector<vector<Point> > contours;
    vector<Vec4i> hierarchy;
    findContours( img, contours, hierarchy, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_TC89_L1, Point(0, 0) );
    for( int i = 0; i< contours.size(); i++ ){
        //show conturs
        Scalar color = Scalar( rng.uniform(0, 255), rng.uniform(0,255), rng.uniform(0,255) );
        drawContours( drawing, contours, i, color, 2, 8, hierarchy, 0, Point() );
        Moments mu = moments( contours[i] , 1 ); // bool 1 ???   
        double eccentricity = getEccentricity( mu ); 
        cout << eccentricity << " " ;
    }
    namedWindow( "Contours", CV_WINDOW_AUTOSIZE );
    imshow( "Contours", drawing );
    cv::waitKey(2000);  
}
