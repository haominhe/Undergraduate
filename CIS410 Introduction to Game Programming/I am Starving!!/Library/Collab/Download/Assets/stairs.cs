using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class stairs : MonoBehaviour {
	static int counter = 0;
	private int maxstairs = 9;
	public GameObject stair;
	// Use this for initialization
	void Start () {
		if (counter <= maxstairs) {
			DoThisStairs ();
		}
	}
	private void DoThisStairs()
	{
		var myPos = transform.position;
		var go = Instantiate (stair, new Vector3 (myPos.x+2, myPos.y + 2, myPos.z), Quaternion.identity)as GameObject;
		go.name = "stair no." + counter;
		counter++;
	}

}
