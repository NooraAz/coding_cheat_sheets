# vectors

initiating a vector

    std::vector <int> my_vector(size);

appending:

    my_vector.push_back(13);
    
iterating:
    
    my_vector[0];
    
    for(vector<int>::iterator i = my_vector.begin(); i!= my_vector.end(); i++)
        cout << *i;

size of vector:

    my_vector.size();
    
zeros vector:

    fill(my_vector.begin(),my_vector.end(),0) 
    
