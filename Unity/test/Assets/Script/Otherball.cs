using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class otherball : MonoBehaviour
{
    MeshRenderer mesh;
    Material mat;
    // Start is called before the first frame update
    void Start()
    {
        mesh = GetComponent<MeshRenderer>();
        mat = mesh.material;
    }

    // Update is called once per frame
    private void OnCollisionEnter(Collision collision)
    {
        if(collision.gameObject.name == "Myball")
            mat.color = new Color32(255, 255, 255, 0);
    }

    private void OnCollisionExit(Collision collision)
    {
        if (collision.gameObject.name == "Myball")
            mat.color = new Color32(255, 0, 0, 0);
    }

}
