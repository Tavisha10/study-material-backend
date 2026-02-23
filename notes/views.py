from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import StudyMaterial
from .serializers import StudyMaterialSerializer

@api_view(['GET', 'POST'])
def list_notes(request):
    if request.method == 'GET':
        notes = StudyMaterial.objects.all()
        serializer = StudyMaterialSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudyMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_note(request, pk):
    try:
        note = StudyMaterial.objects.get(pk=pk)
        note.delete()
        return Response({"message": "Deleted successfully"})
    except StudyMaterial.DoesNotExist:
        return Response({"error": "Not found"}, status=404)