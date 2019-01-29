using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GridCreator : MonoBehaviour
{  
    public float GridHeight;
    public float GridWidth;
    
    float quadHeight;
    float quadWidth;
    public Transform [] markers;
    float x;
    float y;
    float new_oldx;
    float new_oldy;

    int counter = 0;
    const eps = 0.5
    void Start()
    {
        
    }
    void Update()
    {
        if (Abs(x - markers[0].position.x - markers[1].position.x )> eps or Abs(y - markers[0].position.y - markers[1].position.y)>eps){
            new_oldx = markers[0].position.x - markers[1].position.x/x;
            new_oldy = markers[0].position.y - markers[1].position.y/y;
            //Марк запили тут для скэйла для моделек
            x = x * new_oldx;
            y = y * new_oldy;

        }
    }

    void FindCoordinates()
    {
    
       x =Abs(markers[0].position.x - markers[1].position.x);
       y =Abs(markers[0].position.y - markers[1].position.y);
       quadWidth = x/GridWidth;
       quadHeight = y/quadHeight;
    }
    void CreateGrid()
    {
       
    }
}
