using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Base2 : MonoBehaviour {
	private int count;
    public Text countText2;
    public Text winText;

    void Start () {
		count = 0;
        countText2.text = "Count: " + count.ToString();
        winText.text = "";
    }

	void OnTriggerEnter(Collider other)
	{
		if (other.gameObject.CompareTag ("Food")) {
			count += 1;
			other.enabled = false;
            countText2.text = "Count: " + count.ToString();
        }


        if (count >= 2)
        {
            winText.text = "Blue Wins!";
        }
    }
}
