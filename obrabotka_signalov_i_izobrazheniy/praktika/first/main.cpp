#include <string>
#include <fstream>
#include <vector>
#include <cmath>
#include <iostream>
void write_csv(std::string filename, std::vector<double> time, std::vector<double> values){
    std::ofstream file;
    file.open(filename);
    file<<"Time;Value\n";
    for (auto i = 0;i<std::min((int)values.size(),(int)time.size());++i){
        file<<time[i]<<";"<<values[i]<<"\n";
    }
    file.close();
}
double short_time(double t, double T,double phi){
    int i =0;
    while (t>i*T+phi){
        ++i;
    }
    if (i==0){
        return t;
    }
    return t-T*(i-1)-phi;
}
std::vector<double> sin_signal(double F, double T, double N, double phi){
    std::vector<double> result(N*F);
    double t=0;
    for (int i = 0;i<N*F;++i){
        t = (double)i/F;
        result[i] = 512*std::sin(2*M_PI*t/T + phi) + 512;
        
    }
    return result;
}
std::vector<double> triangle_signal(double F, double T, double N, double phi, double tau){
    std::vector<double> result(N*F);
    double t=0;
    double real_t = 0;
    double height = 1024;
    for (int i = 0;i<N*F;++i){
        t = short_time(real_t, T,phi);
        if ((real_t<=phi) || (t>=tau)){
            result[i] = 0;
        }
        else{
            result[i] = height - 2*height*std::abs(tau/2 - t)/tau;
        }
        real_t += 1/F;
    }
    return result;
}

std::vector<double> rectangle_signal(double F, double T, double N, double phi, double tau){
    std::vector<double> result(N*F);
    double t=0;
    double real_t = 0;
    double height = 1024;
    for (int i = 0;i<N*F;++i){
        t = short_time(real_t, T,phi);
        if ((real_t<=phi) || (t>=tau)){
            result[i] = 0;
        }
        else{
            result[i] = height;
        }
        real_t += 1/F;
    }
    return result;
}
std::vector<double> rand_rectangle_signal(double F, double T, double N, double tau){
    std::vector<double> result(N*F);

    double first = (double)(rand()%100)/(10*(double)(rand()%100));
    
    double second = first + tau + (double)rand()/(double)rand();
    double height = 1024;
    double t;
    for (int i = 0; i<N*F;++i){
        t = (double)i/F;
        if (((first<t) && (t<first+tau)) || ((second<t) && (t<second + tau))){
            result[i] = height;
        }
        else{
            result[i] = 0;
        }
        
    }
    return result;
}

std::vector<double> quantize (int quantization_levels, double min, double max, std::vector<double> vector){
    std::vector<double> result(vector.size());
    for (int i=0; i<vector.size();++i){
        result[i] = ((max - min)*vector[i])/quantization_levels + min;
    }
    return result;
}
int main() {
    int quantization_levels=1024;
    double F = 1000;
    double N = 4;
    double T = 1;
    double tau = 0.5;
    double phi = 0.5;
    double min = 0;
    double max = 1;
    std::vector<double>time_array(N*F);
    for (auto i = 0; i<N*F; ++i){
        time_array[i] = i/F;
        

    }
    
    write_csv("sin_data.csv",time_array,quantize(quantization_levels, min, max, sin_signal(F,T,N,phi)));
    write_csv("triangle_data.csv",time_array,quantize(quantization_levels, min, max, triangle_signal(F,T,N,phi, tau)));
    write_csv("rectangle_data.csv",time_array,quantize(quantization_levels, min, max, rectangle_signal(F,T,N,phi, tau)));
    write_csv("rand_rectangle_data.csv",time_array,quantize(quantization_levels, min, max, rand_rectangle_signal(F,T,N,tau)));

}