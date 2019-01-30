using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GridCreator : MonoBehaviour
{  
    public float GridHeight;
    public float GridWidth;
    public Transform [] markers;
    public Transform quad;

    Vector3 time;
    float quadHeight = 1f;
    float quadWidth = 1f;
    const float eps = 0.2f;
 
    float x;
    float y;
    float Ratio_X;
    float Ratio_Y;

    bool needToChangeScale = false;
    void Start()
    {
        FindCoordinates();
        Ratio_X = x/(GridWidth*2);
        Ratio_Y = y/(GridHeight*2);
        CreateGrid();
    }
    void Update()
    {
       FindNewScale();
    }

    void FindCoordinates()
    {
       x = Math.Abs(markers[0].position.x - markers[1].position.x);
       y = Math.Abs(markers[0].position.z - markers[1].position.z);
    }
    
    void CreateGrid()
    {
       for(int i = 0; i < GridWidth; i++)
       {
           for(int j = 0; j < GridHeight; j++)
           {
               Transform cell = Instantiate(quad) as Transform;
               time = cell.localScale;
               time.x *= Ratio_X;
               time.z *= Ratio_Y;
               cell.localScale = time;

               cell.position = markers[0].position + new Vector3(i*2*time.x, 0f, j*2*time.z) + time;

           }
       }
    }
    
    void FindNewScale()
    {
        if (Math.Abs(x - Math.Abs(markers[0].position.x - markers[1].position.x)) > eps || Math.Abs(y - Math.Abs(markers[0].position.z - markers[1].position.z)) > eps)
        {
            Ratio_X = (markers[0].position.x - markers[1].position.x)/x;
            Ratio_Y = (markers[0].position.z - markers[1].position.z)/y;
            needToChangeScale = true;
        }
    }
}
